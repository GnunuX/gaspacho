"""
api's platforms
"""

from bdd.platforms import Platform, OS, Software, Path
from bdd.platforms import OSVersion, SoftwareVersion

# ____________________________________________________________
# Wrapped objects
 
class APIOS(APIWrapper):
    #FIXME: OSVersion should not be here 
    def add_version(self, name, comment=None):
        ver = OSVersion(name=name, comment=comment)
        self._w.versions.append(ver)
        return ver

class APISoftware(APIWrapper):
    def __init__(self, wrap):
        self._w = wrap

    #FIXME: OSVersion should not be here 
    def add_version(self, name, comment=None):
        ver = SoftwareVersion(name=name, comment=comment)
        self._w.versions.append(ver)
        return ver

#---

def add_os(name=None, comment=None):
    """
    add os
    """
    ret = OS(name=name, comment=comment)
    return APIOS(ret)

def add_software(name=None, comment=None):
    """
    add software
    """
    ret = Software(name=name, comment=comment)
    return APISoftware(ret)

def add_platform(osversion=None, softwareversion=None, path=None):
    """
    add platform
    """
    return Platform(osversion=osversion, softwareversion=softwareversion,
            path=path)

def add_path(name, comment=None):
    """
    add path
    """
    return Path(name=name, comment=comment)

def get_platforms():
    """
    list all platforms
    """
    return Platform.query.all()

# vim: ts=4 sw=4 expandtab
