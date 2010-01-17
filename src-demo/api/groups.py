# api's groups

from bdd.groups import Group, Template, User, Computer

def add_group(name, parent=None, comment=u''):
    """
    add group
    """
    if parent == None:
        return Group(name=name, comment=comment)
    else:
        return Group(name=name, parent=parent, comment=comment)

def add_template(name, comment=u''):
    return Template(name=name, comment=comment)

def add_user(name, typ=u'user', comment=u''):
    """
    add user
    """
    return User(name=name, typ=typ, comment=comment)

def add_computer(name, typ=u'ip', comment=u''):
    """
    add computer
    """
    return Computer(name=name, typ=typ, comment=comment)

def get_groups(only_templates=False):
    """
    list group's hierarchy
    """
    groups = {}
    rootgroups = []
    childgroups = {}
    for group in Group.query.all():
        if group.parent == None:
            #list all root group
            rootgroups.append(group)
        else:
            #list all child group
            pname = group.parent.name
            if not childgroups.has_key(pname):
                childgroups[pname] = []
            childgroups[pname].append(group)

    def construct_group(name, cgroups):
        """
        construct group's hierarchy
        """
        groups = []
        if cgroups.has_key(name):
            for group in cgroups[name]:
                tgroup = {'group': group}
                childs = list(construct_group(group.name, cgroups))[0]
                if not childs == []:
                    tgroup['childs'] = childs
                groups.append(tgroup)
        yield groups
    #FIXME
    if only_templates == False:
        groups['groups'] = []
    groups['tpls'] = []
    for group in rootgroups:
        #parse all rootgroups to get childs group
#        if group.template == True:
#            groups['tpls'].append(group)
#        else:
        #FIXME
        if only_templates == False:
            tgroups = {}
            childs = list(construct_group(group.name, childgroups))[0]
            tgroups['group'] = group
            if childs != []:
                tgroups['childs'] = childs
            groups['groups'].append(tgroups)
    return groups

def get_users(typ=None):
    if typ == None:
        return User.query.all()
    else:
        return User.query.filter_by(typ=typ).all()

# vim: ts=4 sw=4 expandtab
