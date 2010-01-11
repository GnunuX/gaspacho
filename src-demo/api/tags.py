# api's tags

from bdd.tags import Tag, ConfLevel

def add_tag(name, typ, description=u''):
    return Tag(name=name, typ=typ, description=description)

def get_conflevel():
    confuser = ConfLevel.query.filter_by(typ=u'confuser').first()
    if confuser == None:
        confuser = ConfLevel(typ=u'confuser', description=u"User's configuration")
    confcomputer = ConfLevel.query.filter_by(typ=u'confcomputer').first()
    if confcomputer == None:
        confcomputer = ConfLevel(typ=u'confcomputer', description=u"Computer's configuration")
    return (confuser, confcomputer)

# vim: ts=4 sw=4 expandtab
