"""
api's choices
"""

from bdd.choices import Choice

def add_choice(rule, group=None, template=None, user=None, platform=None, state=u'off', value=u''):
    """
    add choice with rule + group
    """
    if template != None:
        if group != None:
            print "error"
        Choice(rule=rule, template=template, user=user, platform=platform, state=state, value=value)
    else:
        Choice(rule=rule, group=group, user=user, platform=platform, state=state, value=value)
# vim: ts=4 sw=4 expandtab
