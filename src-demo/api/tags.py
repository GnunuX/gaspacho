# api's tags

from bdd.tags import Tag, ConfLevel

def add_tag(name, typ, description=''):
    return Tag(name=name, typ=typ, description=description)

confuser = ConfLevel(typ='confuser', description="User's configuration")
confcomputer = ConfLevel(typ='conflevel', description="Computer's configuration")

# vim: ts=4 sw=4 expandtab
