# rules

from elixir import *

class Rule(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    defaultstate = Field(UnicodeText)
    defaultvalue = Field(UnicodeText)
    comment = Field(UnicodeText)
    variables = OneToMany('Variable')
    tag = ManyToOne('Tag')
    conflevel = ManyToOne('ConfLevel')
    choices = ManyToMany('Choice')

    def add_variable(self, name, typ, valueon, valueoff, comment=u''):
        var = Variable(name=name, typ=typ, valueon=valueon, valueoff=valueoff, comment=comment)
        self.variables.append(var)
        return var

    def set_tag(self, tag):
        self.tag = tag

    def set_conflevel(self, conflevel):
        self.conflevel = conflevel

    def __repr__(self):
        return 'name: "%s", typ: "%s", defaultstate: "%s", defaultvalue: "%s", comment: "%s"' % (self.name, self.typ, self.defaultstate, self.defaultvalue, self.comment)

class Variable(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    valueon = Field(UnicodeText)
    valueoff = Field(UnicodeText)
    comment = Field(UnicodeText)
    rule = ManyToOne('Rule')
    platforms = ManyToMany('Platform')
    def set_platform(self, platform, comment=u''):
        self.platforms.append(platform)
    def __repr__(self):
        return '["%s", {"typ": "%s", "valueon": "%s", "valueoff": "%s", "comment": "%s"}]' % (self.name, self.typ, self.valueon, self.valueoff, self.comment)

# vim: ts=4 sw=4 expandtab
