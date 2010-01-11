# api's groups

from bdd.groups import Group, User, Computer

def add_group(name, parent=None, template=False, description=u''):
    """
    add group
    """
    if template == True:
        if parent != None:
            raise Exception('group could not be template and have parent')
        return Group(name=name, template=template, description=description)
    else:
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
            rootgroups.append((group.id, group.name, group.template))
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
        groups = []
        if cgroups.has_key(name):
            for yid, yname in cgroups[name]:
                tgroup = {'name': yname, 'id': yid}
                childs = list(construct_group(yname, cgroups))[0]
                if not childs == []:
                    tgroup['childs'] = list(construct_group(yname, cgroups))[0]
                groups.append(tgroup)
        yield groups

    if only_templates == False:
        groups['groups'] = []
    groups['tpls'] = []
    for tid, name, is_tpl in rootgroups:
        #parse all rootgroups to get childs group
        if is_tpl == True:
            groups['tpls'].append({'name': name, 'id': tid})
        else:
            if only_templates == False:
                childs = list(construct_group(name, childgroups))[0]
                tgroup = {'name': name, 'id': tid}
                if childs != []:
                    tgroup['childs'] = childs
                groups['groups'].append(tgroup)
    return groups

def get_users_by_group(group):
    return [(user.id, user.name, user.typ, user.description) for user in group.users]

def get_users(typ=None):
    if typ == None:
        print "pouet"
        uquery = User.query.all()
    else:
        uquery = User.query.filter_by(typ=typ).all()
    return [(user.id, user.name, user.typ, user.description) for user in uquery]

# vim: ts=4 sw=4 expandtab
