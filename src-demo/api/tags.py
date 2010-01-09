# api's tags

from bdd.tags import Tag, ConfLevel

def add_tag(name, typ, description=u''):
    return Tag(name=name, typ=typ, description=description)

confuser = ConfLevel(typ=u'confuser', description=u"User's configuration")
confcomputer = ConfLevel(typ=u'conflevel', description=u"Computer's configuration")

# vim: ts=4 sw=4 expandtab
