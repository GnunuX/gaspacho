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

def list_rules(group=None):
    """
    list rules
    """
    def get_choice(group, rule):
        return Choice.query.filter_by(rule=rule, group=group).first()

    def get_parent_choice(group, rule):
        ret = (None, None, None, None)
        parent = group.parent
        if parent != None:
            choice = get_choice(rule, parent)
            if choice == None:
                ret = get_parent_choice(parent, rule)
            else:
                ret = (parent.name, parent.id, choice.state, choice.value)
        return ret
 
    rules = {}
    for rule in Rule.query.all():
        rid = rule.id
        rules[rid] = {}
        #desciption of the rule
        rules[rid]['rule'] = rule.name
        rules[rid]['description'] = rule.description
        rules[rid]['typ'] = rule.typ
        rules[rid]['platforms'] = {}
        #value and state of this rules
        #if group is set, get herited value and state to parent's group
        #if not, default is set to herited value and state
        rules[rid]['state'] = {}
        rules[rid]['value'] = {}
        rules[rid]['state']['default'] = rule.defaultstate
        if rule.defaultvalue != None:
            rules[rid]['value']['default'] = rule.defaultvalue
        if group != None:
            pname, pid, pstate, pvalue = get_parent_choice(group, rule)
            if not pname == None:
                rules[rid]['state']['herited'] = {'name': pname, 'id': pid, 'state': pstate}
                rules[rid]['value']['herited'] = {'name': pname, 'id': pid, 'value': pvalue}
            choice = get_choice(group, rule)
            if choice != None:
                rules[rid]['state']['current'] = choice.state
                rules[rid]['value']['current'] = choice.value
        for variable in rule.variables:
            for platform in variable.platforms:
                #add platform.id to limit duplication
                rules[rid]['platforms'][platform.id] = [platform.osversion.name,
                     platform.osversion.os.name, platform.softwareversion.name,
                     platform.softwareversion.software.name]
    return rules


def list_variables():
    """
    list variables
    """
    return Variable.query.all()

# vim: ts=4 sw=4 expandtab
