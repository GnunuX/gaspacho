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

def list_rules(group=None, user=None):
    """
    list rules
    """
    def get_choice(group, rule, user):
        return Choice.query.filter_by(rule=rule, group=group, user=user).first()

    def get_depends_choice(group, rule, user):
        for depend in group.depends:
            choice = get_choice(depend, rule, user)
            if choice != None:
                return (depend.name, user, depend.id, choice.state, choice.value)
        if user != None:
            return get_depends_choice(group, rule, None)
        return (None, None, None, None, None)

    def get_parent_choice(group, rule, user):
        parent = group.parent
        if parent != None:
            choice = get_choice(parent, rule, user)
            if choice == None:
                ret = get_depends_choice(parent, rule, user)
                if ret[0] != None:
                    return ret
                return get_parent_choice(parent, rule, user)
            else:
                return (parent.name, user, parent.id, choice.state, choice.value)
        if user != None:
            return get_parent_choice(group, rule, None)
        return (None, None, None, None, None)
 
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
                pname, puser, pid, pstate, pvalue = get_depends_choice(group, rule, user)
                if pname == None:
                    pname, puser, pid, pstate, pvalue = get_parent_choice(group, rule, user)
                if not pname == None:
                    if puser == None:
                        pusern = None
                    else:
                        pusern = puser.name
                    rules[rid]['state']['herited'] = {'name': pname, 'user': pusern, 'id': pid, 'state': pstate}
                    rules[rid]['value']['herited'] = {'name': pname, 'user': pusern, 'id': pid, 'value': pvalue}
                choice = get_choice(group, rule, user)
                if choice != None:
                    rules[rid]['state']['current'] = choice.state
                    rules[rid]['value']['current'] = choice.value
    return rules


def list_variables():
    """
    list variables
    """
    return Variable.query.all()

# vim: ts=4 sw=4 expandtab
