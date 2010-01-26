# groups

from elixir import *

class Group(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    managers = ManyToMany('User', inverse='managedgroups')
    computers = ManyToMany('Computer')
    users = ManyToMany('User', inverse='groups')
    choices = OneToMany('Choice')
    parent = ManyToOne('Group', inverse='childs')
    childs = OneToMany('Group')
    depends = ManyToMany('Template')
    softwares = ManyToMany('Software')

    def __repr__(self):
        return "{'name': '%s', 'comment': '%s'}"  % (self.name, self.comment)

class Template(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
#    managers = ManyToMany('User', inverse='managedgroups')
#    users = ManyToMany('User', inverse='groups')
    depends = ManyToMany('Group')
    choices = OneToMany('Choice')
    softwares = ManyToMany('Software')

#    def __repr__(self):
#        return '{name: "%s", comment: "%s"}' % (self.name, self.comment)

class User(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    comment = Field(UnicodeText)
    groups = ManyToMany('Group')
    managedgroups = ManyToMany('Group')
    choices = ManyToMany('Choice')

    def __repr__(self):
        return '{name: "%s", typ: "%s", comment: "%s"}' % (self.name, self.typ,
                self.comment)

class Computer(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    comment = Field(UnicodeText)
    groups = ManyToMany('Group')

    def __repr__(self):
        return '{"name": "%s", typ: "%s", comment: "%s"}' % (self.name, self.typ,
                self.comment)

# vim: ts=4 sw=4 expandtab
