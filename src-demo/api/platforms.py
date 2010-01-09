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

def list_platforms():
    """
    list all platforms
    """
    platforms = {}
    for platform in Platform.query.all():
        num = platform.id
        platforms[num] = {}
        platforms[num]['os'] = [platform.osversion.os.name,
                platform.osversion.name]
        platforms[num]['software'] = [platform.softwareversion.software.name,
                platform.softwareversion.name]
    return platforms

# vim: ts=4 sw=4 expandtab
