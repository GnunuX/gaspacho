from elixir import *
from api.rules import get_rules
from api.platforms import get_platforms
from api.groups import get_groups, get_users, get_group_by_id
from api.categories import get_categories, get_category_by_id
#
from api.choices import add_choice
#from api.tags import confuser, confcomputer
from api.categories import add_tag


import json

metadata.bind = "sqlite:///gaspacho.sqlite"
setup_all()

def data_groups_tree(id):
    ret = []
    ogroup = get_group_by_id(id)
    for group in get_groups(ogroup):
        cls = 'group'
        ret.append({"text": group.name, "id": "g"+str(group.id), "cls": cls})
    for user in ogroup.users:
        ret.append({"text": user.name, "id": "u"+str(user.id), "cls": user.typ})
    return json.dumps(ret)

def data_categories_paned():
    ret = []
    for category in get_categories():
        ret.append({"text": category.name, "id": category.id})
    print json.dumps(ret)

def data_rules(conflevel, groupid, categoryid):
    #grouping
    import pprint
    pp = pprint.PrettyPrinter(depth=7)
    group = get_group_by_id(groupid)
    category = get_category_by_id(categoryid)
#    pp.pprint(get_rules(conflevel=conflevel, group=group))
    ret = []
    for tag in get_rules(conflevel=conflevel, group=group, category=category):
        ntag = tag['tag'].name
        for rule in tag['rules']:
            if rule['choice'].has_key('herited'):
                sherited = rule['choice']['herited']['choice'].state
                vherited = rule['choice']['herited']['choice'].value
            else:
                sherited = None
                vherited = None
            ret.append({'name': rule['rule'].name, 'herited': {'state': sherited, 'value': vherited}})
    print json.dumps(ret)

#FIXME
#from api.categories import get_conflevel
#confuser, confcomputer = get_conflevel()
#print data_groups_tree(1)
#print data_categories_paned()
#print data_rules(confcomputer, 1, 2)


# vim: ts=4 sw=4 expandtab
