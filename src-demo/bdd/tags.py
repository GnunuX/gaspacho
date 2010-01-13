from elixir import *

class Tag(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    rules = OneToMany('Rule')
    def __repr__(self):
        return 'name: "%s", description: "%s"' % (self.name, self.description)

class Category(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    rules = OneToMany('Rule')
    def __repr__(self):
        return 'name: "%s", description: "%s"' % (self.name, self.description)

class ConfLevel(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    rules = OneToMany('Rule')
    def __repr__(self):
        return 'name: "%s", description: "%s"' % (self.name, self.description)

# vim: ts=4 sw=4 expandtab
