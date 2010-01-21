# api's tags

from bdd.categories import Tag, Category, ConfLevel

# ____________________________________________________________
# Wrapped objects
 
class APICategory:
    def __init__(self, wrap):
        self._w = wrap
      
    def add_tag(self, tag):
        self._w.tags.append(tag)
#---

def add_tag(name, comment=u''):
    return Tag(name=name, comment=comment)

def add_category(name, comment=u''):
    ret = Category(name=name, comment=comment)
    return APICategory(ret)

def get_conflevel():
    confuser = ConfLevel.query.filter_by(name=u'confuser').first()
    if confuser == None:
        confuser = ConfLevel(name=u'confuser', comment=u"User's configuration")
    confcomputer = ConfLevel.query.filter_by(name=u'confcomputer').first()
    if confcomputer == None:
        confcomputer = ConfLevel(name=u'confcomputer', comment=u"Computer's configuration")
    return (confuser, confcomputer)

# vim: ts=4 sw=4 expandtab
