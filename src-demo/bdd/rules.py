# rules

from elixir import *

class Rule(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    defaultstate = Field(UnicodeText)
    defaultvalue = Field(UnicodeText)
    description = Field(UnicodeText)
    variables = OneToMany('Variable')
    tags = ManyToMany('Tag')
    conflevel = ManyToOne('ConfLevel')
    choices = ManyToMany('Choice')

    def add_variable(self, name, typ, valueon, valueoff, description=u''):
        var = Variable(name=name, typ=typ, valueon=valueon, valueoff=valueoff, description=description)
        self.variables.append(var)
        return var

    def add_tag(self, tag):
        self.tags.append(tag)

    def set_conflevel(self, conflevel):
        self.conflevel = conflevel

    def __repr__(self):
        return '["%s", {"typ": "%s", "defaultstate": "%s", "defaultvalue": "%s", "description": "%s"}]' % (self.name, self.typ, self.defaultstate, self.defaultvalue, self.description)

class Variable(Entity):
    rule = ManyToOne('Rule')
    platforms = ManyToMany('Platform')
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    valueon = Field(UnicodeText)
    valueoff = Field(UnicodeText)
    description = Field(UnicodeText)
    def set_platform(self, platform, description=u''):
        self.platforms.append(platform)
    def __repr__(self):
        return '["%s", {"typ": "%s", "valueon": "%s", "valueoff": "%s", "description": "%s"}]' % (self.name, self.typ, self.valueon, self.valueoff, self.description)

# vim: ts=4 sw=4 expandtab
