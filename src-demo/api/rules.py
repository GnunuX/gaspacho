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
        return Choice.query.filter_by(rule=rule, group=group, user=user).all()

    def get_depends_choice(group, rule, user):
        for depend in group.depends:
            choices = get_choice(depend, rule, user)
            if choices != []:
                ret = []
                for choice in choices:
                    ret.append((depend, user, choice))
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
                    ret.append((parent, user, choice))
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
    for rule in Rule.query.filter_by(conflevel=conflevel).all():
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
            rid = rule.id
            rules[rid] = {}
            rules[rid]['rule'] = rule
            rules[rid]['platforms'] = tplatform
            if group != None:
                rules[rid]['choice'] = {}
                #if group is set, get current and herited choice
                choices = get_depends_choice(group, rule, user)
                if choices == None:
                    choices = get_parent_choice(group, rule, user)
                if not choices == None:
                    rules[rid]['choice']['herited'] = []
                    for choice in choices:
                        pgroup = choice[0]
                        puser = choice[1]
                        pchoice = choice[2]
                        rules[rid]['choice']['herited'].append({'group': pgroup, 'user': puser, 'choice': pchoice})
                choices = get_choice(group, rule, user)
                if choices == []:
                    choices = get_choice(group, rule, None)
                if choices != []:
                    rules[rid]['choice']['current'] = [choice for choice in choices]
    return rules


def get_variables():
    """
    list variables
    """
    return Variable.query.all()

# vim: ts=4 sw=4 expandtab
