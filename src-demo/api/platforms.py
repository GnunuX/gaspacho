"""
api's platforms
"""

from bdd.platforms import Platform, OS, Software, Path

def add_os(name=None, comment=None):
    """
    add os
    """
    return OS(name=name, comment=comment)

def add_software(name=None, comment=None):
    """
    add software
    """
    return Software(name=name, comment=comment)

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
