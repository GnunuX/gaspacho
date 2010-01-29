"""
api's choices
"""

from bdd.choices import Choice

def set_choice(rule, group=None, template=None, user=None, platform=None, state=u'off', value=u''):
    """
    add choice with rule + group
    """
    if template != None:
        if group != None:
            print "error"
        ret = Choice.query.filter_by(rule=rule, template=template, user=user, platform=platform).first()
        if ret != None:
            ret.state=state
            ret.value=value
            return ret
        else:
            return Choice(rule=rule, template=template, user=user, platform=platform, state=state, value=value)
    else:
        ret = Choice.query.filter_by(rule=rule, group=group, user=user, platform=platform).first()
        if ret != None:
            ret.state=state
            ret.value=value
            return ret
        else:
            return Choice(rule=rule, group=group, user=user, platform=platform, state=state, value=value)
# vim: ts=4 sw=4 expandtab
