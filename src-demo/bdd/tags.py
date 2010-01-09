from elixir import *

class Tag(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    description = Field(UnicodeText)
    rules = ManyToMany('Rule')

class ConfLevel(Entity):
    typ = Field(UnicodeText)
    description = Field(UnicodeText)
    rules = OneToMany('Rule')

# vim: ts=4 sw=4 expandtab
