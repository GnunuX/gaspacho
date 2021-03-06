# _*_ coding: utf-8 _*_
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

    def __repr__(self):
        ret = 'name: "%s", typ: "%s", defaultstate: "%s", defaultvalue: "%s", \
                    comment: "%s"' % (self.name, self.typ, self.defaultstate,
                    self.defaultvalue, self.comment)
        return ret.encode('utf-8')

class Variable(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    valueon = Field(UnicodeText)
    valueoff = Field(UnicodeText)
    comment = Field(UnicodeText)
    rule = ManyToOne('Rule')
    platforms = ManyToMany('Platform')

    def __repr__(self):
        return '["%s", {"typ": "%s", "valueon": "%s", "valueoff": "%s", \
                    "comment": "%s"}]' % (self.name, self.typ, self.valueon,
                    self.valueoff, self.comment)

# vim: ts=4 sw=4 expandtab
