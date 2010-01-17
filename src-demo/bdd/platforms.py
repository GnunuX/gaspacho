from elixir import *

class OS(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    versions = OneToMany('OSVersion')
    def add_version(self, name, description=None):
        ver = OSVersion(name=name, description=description)
        self.versions.append(ver)
        return ver

class Software(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    versions = OneToMany('SoftwareVersion')
    templates = ManyToMany('Group')
    def add_version(self, name, description=None):
        ver = SoftwareVersion(name=name, description=description)
        self.versions.append(ver)
        return ver

class OSVersion(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    platform = OneToMany('Platform')
    os = ManyToOne('OS')

class SoftwareVersion(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    platform = OneToMany('Platform')
    software = ManyToOne('Software')

class Path(Entity):
    name = Field(UnicodeText)
    description = Field(UnicodeText)
    platforms = OneToMany('Platform')

class Platform(Entity):
    osversion = ManyToOne('OSVersion')
    softwareversion = ManyToOne('SoftwareVersion')
    path = ManyToOne('Path')
    variables = ManyToMany('Variable')
    choices = OneToMany('Choice') 
    def __repr__(self):
        return 'osname: "%s", osversion: "%s", softwarename: "%s", softwareversion: "%s", path: "%s"' % (self.osversion.os.name, self.osversion.name, self.softwareversion.software.name, self.softwareversion.name, self.path.name)

# vim: ts=4 sw=4 expandtab
