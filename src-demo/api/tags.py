# api's tags

from bdd.tags import Tag, Category, ConfLevel

def add_tag(name, description=u''):
    return Tag(name=name, description=description)

def add_category(name, description=u''):
    return Category(name=name, description=description)

def get_conflevel():
    confuser = ConfLevel.query.filter_by(name=u'confuser').first()
    if confuser == None:
        confuser = ConfLevel(name=u'confuser', description=u"User's configuration")
    confcomputer = ConfLevel.query.filter_by(name=u'confcomputer').first()
    if confcomputer == None:
        confcomputer = ConfLevel(name=u'confcomputer', description=u"Computer's configuration")
    return (confuser, confcomputer)

# vim: ts=4 sw=4 expandtab
