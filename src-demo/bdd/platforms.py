from elixir import *

class OS(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    versions = OneToMany('OSVersion')
    def add_version(self, name, comment=None):
        ver = OSVersion(name=name, comment=comment)
        self.versions.append(ver)
        return ver

class Software(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    versions = OneToMany('SoftwareVersion')
    templates = ManyToMany('Group')
    def add_version(self, name, comment=None):
        ver = SoftwareVersion(name=name, comment=comment)
        self.versions.append(ver)
        return ver

class OSVersion(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    platform = OneToMany('Platform')
    os = ManyToOne('OS')

class SoftwareVersion(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    platform = OneToMany('Platform')
    software = ManyToOne('Software')

class Path(Entity):
    name = Field(UnicodeText)
    comment = Field(UnicodeText)
    platforms = OneToMany('Platform')

class Platform(Entity):
    osversion = ManyToOne('OSVersion')
    softwareversion = ManyToOne('SoftwareVersion')
    path = ManyToOne('Path')
    variables = ManyToMany('Variable')
    choices = OneToMany('Choice') 
    def __repr__(self):
        if self.softwareversion != None:
            soft = 'software: "%s-%s", ' % (self.softwareversion.software.name, self.softwareversion.name)
        else:
            soft = ''
        return '%sos: "%s-%s", path: "%s"' % (soft, self.osversion.os.name, self.osversion.name, self.path.name)

# vim: ts=4 sw=4 expandtab
