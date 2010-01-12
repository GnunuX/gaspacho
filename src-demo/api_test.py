from elixir import *
from api.rules import get_rules
from api.platforms import get_platforms
from api.groups import get_groups, get_users
#
from api.choices import add_choice
#from api.tags import confuser, confcomputer
from api.tags import add_tag

import pprint

metadata.bind = "sqlite:///gaspacho.sqlite"
setup_all()
from api.tags import get_conflevel
#--BEURK--
from bdd.groups import Group, User
mathroom = Group.query.filter_by(id=4).first()
tplfirefox = Group.query.filter_by(id=3).first()
student = User.query.filter_by(id=1).first()
confuser, confcomputer = get_conflevel()

pp = pprint.PrettyPrinter(depth=7)
#list all rules with default settings for confuser
#pp.pprint(get_rules(confcomputer))

#list all rules with choices
#pp.pprint(get_rules(confuser, group=mathroom, user=student))
#pp.pprint(get_rules(confcomputer, group=tplfirefox))

#list groups
pp.pprint(get_groups())
pp.pprint(get_groups(only_templates=True))

#list all users
#pp.pprint(get_users())
#pp.pprint(get_users(u'group'))
#pp.pprint(get_users(u'user'))

#list platforms
#pp.pprint(get_platforms())

# vim: ts=4 sw=4 expandtab
