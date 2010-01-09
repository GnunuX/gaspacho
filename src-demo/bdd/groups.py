# groups

from elixir import *

class Group(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    managers = ManyToMany('User', inverse='managedgroups')
    computers = ManyToMany('Computer')
    users = ManyToMany('User', inverse='groups')
    choices = OneToMany('Choice')
    parent = ManyToOne('Group', inverse='childs')
    childs = OneToMany('Group')

    def set_computer(self, computer):
        self.computers.append(computer)

    def set_user(self, user):
        self.users.append(user)

    def set_manager(self, user):
        self.managers.append(user)

class User(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    description = Field(UnicodeText)
    groups = ManyToMany('Group')
    managedgroups = ManyToMany('Group')
    choices = ManyToMany('Choice')

class Computer(Entity):
    name = Field(UnicodeText)
    typ = Field(UnicodeText)
    description = Field(UnicodeText)
    groups = ManyToMany('Group')

# vim: ts=4 sw=4 expandtab
