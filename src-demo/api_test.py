from elixir import *
from api.rules import get_rules
from api.platforms import get_platforms
from api.groups import get_groups, get_users, get_users_by_group
#
from api.choices import add_choice
from api.tags import add_tag, confuser, confcomputer

import pprint

metadata.bind = "sqlite:///gaspacho.sqlite"
setup_all()
#--BEURK--
from bdd.groups import Group, User
mathroom = Group.query.filter_by(id=4).first()
tplfirefox = Group.query.filter_by(id=3).first()
student = User.query.filter_by(id=1).first()

pp = pprint.PrettyPrinter(depth=7)
#list all rules with default settings
#pp.pprint(get_rules())

#list all rules with choices
#pp.pprint(get_rules())
#pp.pprint(get_rules(user=student))
#pp.pprint(get_rules(group=mathroom, user=student))
#pp.pprint(get_rules(group=tplfirefox))

#list groups
#pp.pprint(get_groups())
#pp.pprint(get_groups(only_templates=True))

#list users in group
pp.pprint(get_users_by_group(mathroom))

#list all users
pp.pprint(get_users())
pp.pprint(get_users(u'group'))
pp.pprint(get_users(u'user'))

#list platforms
#pp.pprint(get_platforms())

# vim: ts=4 sw=4 expandtab
