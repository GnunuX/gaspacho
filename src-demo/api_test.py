from elixir import *
from api.rules import list_rules
from api.platforms import list_platforms
from api.groups import list_groups
#
from api.choices import add_choice
from api.tags import add_tag, confuser, confcomputer

#--BEURK--
from bdd.groups import Group

import pprint

metadata.bind = "sqlite:///gaspacho.sqlite"
setup_all()

pp = pprint.PrettyPrinter(depth=6)
#list all rules with default settings
#print pp.pprint(list_rules())

#list all rules with choices for mathroom
mathroom = Group.query.filter_by(id=3).first()
print pp.pprint(list_rules(mathroom))

#list groups
#print pp.pprint(list_groups())

#list platforms
#print pp.pprint(list_platforms())

# vim: ts=4 sw=4 expandtab
