# api's tags

from bdd.tags import Tag, Category, ConfLevel

def add_tag(name, comment=u''):
    return Tag(name=name, comment=comment)

def add_category(name, comment=u''):
    return Category(name=name, comment=comment)

def get_conflevel():
    confuser = ConfLevel.query.filter_by(name=u'confuser').first()
    if confuser == None:
        confuser = ConfLevel(name=u'confuser', comment=u"User's configuration")
    confcomputer = ConfLevel.query.filter_by(name=u'confcomputer').first()
    if confcomputer == None:
        confcomputer = ConfLevel(name=u'confcomputer', comment=u"Computer's configuration")
    return (confuser, confcomputer)

# vim: ts=4 sw=4 expandtab
