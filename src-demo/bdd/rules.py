# rules

from elixir import *

class Rule(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    defaultstate = Field(UnicodeText)
    defaultvalue = Field(UnicodeText)
    description = Field(UnicodeText)
    variables = OneToMany('Variable')
    tag = ManyToOne('Tag')
    #FIXME
    category = ManyToOne('Category')
    conflevel = ManyToOne('ConfLevel')
    choices = ManyToMany('Choice')

    def add_variable(self, name, typ, valueon, valueoff, description=u''):
        var = Variable(name=name, typ=typ, valueon=valueon, valueoff=valueoff, description=description)
        self.variables.append(var)
        return var

    def set_tag(self, tag):
        self.tag = tag

    def set_category(self, category):
        self.category = category

    def set_conflevel(self, conflevel):
        self.conflevel = conflevel

    def __repr__(self):
        return 'name: "%s", typ: "%s", defaultstate: "%s", defaultvalue: "%s", description: "%s"' % (self.name, self.typ, self.defaultstate, self.defaultvalue, self.description)

class Variable(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    valueon = Field(UnicodeText)
    valueoff = Field(UnicodeText)
    #FIXME: comment
    description = Field(UnicodeText)
    rule = ManyToOne('Rule')
    platforms = ManyToMany('Platform')
    def set_platform(self, platform, description=u''):
        self.platforms.append(platform)
    def __repr__(self):
        return '["%s", {"typ": "%s", "valueon": "%s", "valueoff": "%s", "description": "%s"}]' % (self.name, self.typ, self.valueon, self.valueoff, self.description)

# vim: ts=4 sw=4 expandtab
