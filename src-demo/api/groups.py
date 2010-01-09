# api's groups

from bdd.groups import Group, User, Computer

def add_group(name, parent=None, description=u''):
    """
    add group
    """
    if parent == None:
        return Group(name=name, description=description)
    else:
        return Group(name=name, parent=parent, description=description)

def add_user(name, typ=u'user', description=u''):
    """
    add user
    """
    return User(name=name, typ=typ, description=description)

def add_computer(name, typ=u'ip', description=u''):
    """
    add computer
    """
    return Computer(name=name, typ=typ, description=description)

def list_groups():
    """
    list group's hierarchy
    """
    groups = {}
    rootgroups = []
    childgroups = {}
    for group in Group.query.all():
        if group.parent == None:
            #list all root group
            rootgroups.append((group.id, group.name))
        else:
            #list all child group
            pname = group.parent.name
            if not childgroups.has_key(pname):
                childgroups[pname] = []
            childgroups[pname].append((group.id, group.name))

    def construct_group(name, cgroups):
        """
        construct group's hierarchy
        """
        groups = {}
        if cgroups.has_key(name):
            for yid, yname in cgroups[name]:
                groups[yname] = {}
                groups[yname]['id'] = yid
                childs = list(construct_group(yname, cgroups))[0]
                if not childs == {}:
                    groups[yname]['childs'] = list(construct_group(yname, cgroups))[0]
        yield groups

    for tid, name in rootgroups:
        #parse all rootgroups to get childs group
        groups[name] = {}
        groups[name]['id'] = tid
        groups[name]['childs'] = list(construct_group(name, childgroups))[0]
 
    return groups

# vim: ts=4 sw=4 expandtab
