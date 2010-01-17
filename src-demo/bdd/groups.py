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
    depends = ManyToMany('Group')
    softwares = ManyToMany('Software')

    def add_computer(self, computer):
        self.computers.append(computer)

    def add_user(self, user):
        self.users.append(user)

    def add_manager(self, user):
        self.managers.append(user)

    def add_depend(self, depend):
        self.depends.append(depend)

    def add_software(self, software):
        self.softwares.append(software)
    def __repr__(self):
        return 'name: "%s", description: "%s", template: "%s"' % (self.name, self.description, self.template)

class Template(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    managers = ManyToMany('User', inverse='managedgroups')
    users = ManyToMany('User', inverse='groups')
    choices = OneToMany('Choice')
    softwares = ManyToMany('Software')

    def add_user(self, user):
        self.users.append(user)

    def add_manager(self, user):
        self.managers.append(user)

    def add_software(self, software):
        self.softwares.append(software)

    def __repr__(self):
        return 'name: "%s", description: "%s", template: "%s"' % (self.name, self.description, self.template)

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
