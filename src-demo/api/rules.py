"""
api's rules
"""

from bdd.rules import Rule, Variable
from bdd.choices import Choice
from bdd.categories import Tag
from api.wrapper import APIWrapper
 
class APIRule(APIWrapper):
 
    def add_variable(self, var):
        self._w.variables.append(var)

    def set_tag(self, tag):
        self._w.tag = tag

    def set_conflevel(self, conflevel):
        self._w.conflevel = conflevel

class APIVariable(APIWrapper):
      
    def add_platform(self, platform, comment=u''):
        self._w.platforms.append(platform)


def add_rule(name, typ, defaultstate=u'off', defaultvalue=None,
        comment=u''):
    """
    add rule
    """
    rule = Rule(name=name, typ=typ, defaultstate=defaultstate, defaultvalue=defaultvalue, comment=comment)
    return APIRule(rule)


def add_variable(name, typ, valueon, valueoff, comment=u''):
    variable = Variable(name=name, typ=typ, valueon=valueon, valueoff=valueoff, comment=comment)
    return APIVariable(variable)

def get_rules(conflevel=None, group=None, category=None, template=None, user=None):
    """
    list rules
    """
    #get_choice: return the choice for a group/rule/user
    def get_choice(group, rule, user):
        return Choice.query.filter_by(rule=rule, group=group, user=user).first()

    #get_template_choice: return the choice for a template/rule/user
    def get_template_choice(template, rule, user):
        return Choice.query.filter_by(rule=rule, template=template, user=user).first()

    def get_depends_choice(group, rule, user):
        for depend in group.depends:
            choice = get_template_choice(depend, rule, user)
            if choice != None:
                return choice
        if user != None:
            return get_depends_choice(group, rule, None)
        return None

    def get_parent_choice(group, rule, user):
        parent = group.parent
        if parent != None:
            choice = get_choice(parent, rule, user)
            if choice == None:
                ret = get_depends_choice(parent, rule, user)
                if ret != None:
                    return ret
                return get_parent_choice(parent, rule, user)
            else:
                return choice
        if user != None:
            return get_parent_choice(group, rule, None)
        return None
 
    rules = []
    #collect softwares name associate to this group
    softwares = []
    if group != None:
        if group.softwares != None:
            for software in group.softwares:
                softwares.append(str(software.name))

    for tag in Tag.query.filter_by(category=category):
        trules = []
        if conflevel == None:
            qrules = Rule.query.filter_by(tag=tag).all()
        else:
            qrules = Rule.query.filter_by(conflevel=conflevel, tag=tag).all()
        for rule in qrules:
            if softwares == []:
                is_software = True
            else:
                is_software = False
            tplatform = []
            tplatformadded = []
            for variable in rule.variables:
                for platform in variable.platforms:
                    if softwares != [] and platform.softwareversion.software.name in softwares:
                        is_software = True
                    #not add platform two times
                    if not platform.id in tplatformadded:
                        tplatformadded.append(platform.id)
                        tplatform.append(platform)

            if is_software == True:
                trule = {}
                trule['rule'] = rule
                trule['platforms'] = tplatform
                if group != None:
                    if template != None:
                        print "error template"
                    trule['choice'] = {}
                    #if group is set, get current and herited choice
                    choice = get_depends_choice(group, rule, user)
                    if choice == None:
                        choice = get_parent_choice(group, rule, user)
                    if not choice == None:
                        trule['choice']['herited'] = choice
                if group != None or template != None:
                    if group == None:
                        choice = get_template_choice(template, rule, user)
                    else:
                        choice = get_choice(group, rule, user)
                    if choice == "" and user != None:
                        if group == None:
                            choice = get_template_choice(template, rule, None)
                        else:
                            choice = get_choice(group, rule, None)
                    if choice != None:
                        trule['choice']['current'] = choice
                trules.append(trule)
        if trules != []:
            rules.append({'tag': tag, 'rules': trules})
    return rules

def get_rule_by_id(id):
    if type(id) != int:
        raise Exception("not an integer")
    ret = Rule.query.filter_by(id=id).first()
    if ret == None:
        raise Exception("not a valid id")
    return ret

def get_variables():
    """
    list variables
    """
    return Variable.query.all()

# vim: ts=4 sw=4 expandtab
