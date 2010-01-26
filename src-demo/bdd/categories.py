from elixir import *

class Tag(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    rules = OneToMany('Rule')
    category = ManyToOne('Category')
    def __repr__(self):
        return '{"name": "%s", "comment": "%s"}' % (self.name, self.comment)

class Category(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    tags = OneToMany('Tag')

    def __repr__(self):
        return '{"name": "%s", "comment": "%s"}' % (self.name, self.comment)

class ConfLevel(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    rules = OneToMany('Rule')
    def __repr__(self):
        return '{"name": "%s", "comment": "%s"}' % (self.name, self.comment)

# vim: ts=4 sw=4 expandtab
