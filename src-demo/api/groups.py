# api's groups

from bdd.groups import Group, Template, User, Computer

# ____________________________________________________________
# Wrapped objects
 
class APIGroup(APIWrapper):
    def add_computer(self, computer):
        self._w.computers.append(computer)

    def add_user(self, user):
        self._w.users.append(user)

    def add_manager(self, user):
        self._w.managers.append(user)

    def add_depend(self, template):
        self._w.depends.append(template)

    def add_software(self, software):
        self._w.softwares.append(software)

class APITemplate(APIWrapper):
    def add_user(self, user):
        self._w.users.append(user)

    def add_manager(self, user):
        self._w.managers.append(user)

    def add_software(self, software):
        self._w.softwares.append(software)

def add_group(name, parent=None, comment=u''):
    """
    add group
    """
    if parent == None:
        ret = Group(name=name, comment=comment)
    else:
        ret = Group(name=name, parent=parent, comment=comment)
    return APIGroup(Group)

def add_template(name, comment=u''):
    ret = Template(name=name, comment=comment)
    return APITemplate(Template)

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
    groups['tpls'] = []
    for template in Template.query.all():
        groups['tpls'].append(template)
    if only_templates == True:
        return groups
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
    groups['groups'] = []
    for group in rootgroups:
        #parse all rootgroups to get childs group
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
