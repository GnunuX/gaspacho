"""
api's platforms
"""

from bdd.platforms import Platform, OS, Software, Path

def add_os(name=None, description=None):
    """
    add os
    """
    return OS(name=name, description=description)

def add_software(name=None, description=None):
    """
    add software
    """
    return Software(name=name, description=description)

def add_platform(osversion=None, softwareversion=None, path=None):
    """
    add platform
    """
    return Platform(osversion=osversion, softwareversion=softwareversion,
            path=path)

def add_path(name, description=None):
    """
    add path
    """
    return Path(name=name, description=description)

def get_platforms():
    """
    list all platforms
    """
    return Platform.query.all()

# vim: ts=4 sw=4 expandtab
