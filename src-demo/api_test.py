from elixir import *
from api.rules import list_rules
from api.platforms import list_platforms
from api.groups import list_groups
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
#print pp.pprint(list_rules())

#list all rules with choices
#print pp.pprint(list_rules())
#print pp.pprint(list_rules(user=student))
#print pp.pprint(list_rules(group=mathroom, user=student))
list_rules(group=tplfirefox)

#list groups
#print pp.pprint(list_groups())
#print pp.pprint(list_groups(only_templates=True))

#list platforms
#print pp.pprint(list_platforms())

# vim: ts=4 sw=4 expandtab
