"""
api's rules
"""

from bdd.rules import Rule, Variable
from bdd.choices import Choice

def add_rule(name, typ, defaultstate=u'off', defaultvalue=None,
        description=u''):
    """
    add rule
    """
    return Rule(name=name, typ=typ, defaultstate=defaultstate,
           defaultvalue=defaultvalue, description=description)

def get_rules(conflevel, group=None, user=None):
    """
    list rules
    """
    def get_choice(group, rule, user):
        return Choice.query.filter_by(rule=rule, group=group, user=user, conflevel=conflevel).all()

    def get_depends_choice(group, rule, user):
        for depend in group.depends:
            choices = get_choice(depend, rule, user)
            if choices != []:
                ret = []
                for choice in choices:
                    ret.append((depend.name, user, depend.id, choice.platform, choice.state, choice.value))
                return ret
        if user != None:
            return get_depends_choice(group, rule, None)
        return None

    def get_parent_choice(group, rule, user):
        parent = group.parent
        if parent != None:
            choices = get_choice(parent, rule, user)
            if choices == []:
                ret = get_depends_choice(parent, rule, user)
                if ret != None:
                    return ret
                return get_parent_choice(parent, rule, user)
            else:
                ret = []
                for choice in choices:
                    ret.append((parent.name, user, parent.id, choice.platform, choice.state, choice.value))
                return ret
        if user != None:
            return get_parent_choice(group, rule, None)
        return None
 
    rules = {}
    softwares = []
    if group != None:
        if group.softwares != None:
            for software in group.softwares:
                softwares.append(str(software.name))
    for rule in Rule.query.all():
        if softwares == []:
            is_software = True
        else:
            is_software = False
        tplatform = {}
        for variable in rule.variables:
            for platform in variable.platforms:
                if softwares != [] and platform.softwareversion.software.name in softwares:
                    is_software = True
                #add platform.id to limit duplication
                tplatform[platform.id] = [platform.osversion.name,
                     platform.osversion.os.name, platform.softwareversion.name,
                     platform.softwareversion.software.name]

        if is_software == True:
            rid = rule.id
            rules[rid] = {}
            #desciption of the rule
            rules[rid]['rule'] = rule.name
            rules[rid]['description'] = rule.description
            rules[rid]['typ'] = rule.typ
            rules[rid]['platforms'] = tplatform
            #value and state of this rules
            #if group is set, get herited value and state to parent's group
            #if not, default is set to herited value and state
            rules[rid]['state'] = {}
            rules[rid]['value'] = {}
            rules[rid]['state']['default'] = rule.defaultstate
            if rule.defaultvalue != None:
                rules[rid]['value']['default'] = rule.defaultvalue
            if group != None:
                choices = get_depends_choice(group, rule, user)
                if choices == None:
                    choices = get_parent_choice(group, rule, user)
                if not choices == None:
                    for choice in choices:
                        pname = choice[0]
                        puser = choice[1]
                        pid = choice[2]
                        pplatformid = choice[3]
                        pstate = choice[4]
                        pvalue = choice[5]
                        if puser == None:
                            pusern = None
                        else:
                            pusern = puser.name
                        rules[rid]['state']['herited'] = {'name': pname, 'user': pusern, 'id': pid, 'state': pstate}
                        if pplatformid != None:
                            rules[rid]['state']['herited']['platformid'] = pplatformid
                        rules[rid]['value']['herited'] = {'name': pname, 'user': pusern, 'id': pid, 'value': pvalue}
                        if pplatformid != None:
                            rules[rid]['value']['herited']['platformid'] = pplatformid
                choices = get_choice(group, rule, user)
                if choices == []:
                    choices = get_choice(group, rule, None)
                if choices != []:
                    rules[rid]['state']['current'] = []
                    rules[rid]['value']['current'] = []
                    for choice in choices:
                        if choice.platform == None:
                            platform = 0
                        else:
                            platform = choice.platform.id
                        rules[rid]['state']['current'].append({platform: choice.state})
                        rules[rid]['value']['current'].append({platform: choice.value})
    return rules


def get_variables():
    """
    list variables
    """
    return Variable.query.all()

# vim: ts=4 sw=4 expandtab
