from twisted.web import server, resource, static, server
from twisted.internet import reactor
from elixir import *
from api.rules import get_rules, get_rule_by_id
from api.platforms import get_platforms
from api.groups import get_groups, get_users, get_group_by_id, get_user_by_id
from api.categories import get_categories, get_category_by_id
#
from api.choices import set_choice
from api.categories import add_tag

import json

metadata.bind = "sqlite:///gaspacho.sqlite"
setup_all()

def data_groups_tree(id=None):
    ret = []
    if id == None:
        ogroup = None
    else:
        ogroup = get_group_by_id(id)
    for group in get_groups(ogroup):
        cls = 'group'
        ret.append({"text": group.name, "id": group.id, "cls": cls})
    if ogroup != None:
        for user in ogroup.users:
            ret.append({"text": user.name, "id": user.id, "cls": user.typ})
    return json.dumps(ret)

def data_categories_paned():
    ret = []
    for category in get_categories():
        ret.append({"text": category.name, "id": category.id})
    return json.dumps(ret)

def data_rules(categoryid, groupid, userid=None):
    #grouping
    group = get_group_by_id(groupid)
    category = get_category_by_id(categoryid)
    if userid != None:
        user = get_user_by_id(userid)
        rules = get_rules(conflevel=confuser, group=group, category=category, user=user)
    else:
        rules = get_rules(group=group, category=category)
    ret = []
    for tag in rules:
        ntag = tag['tag'].name
        for rule in tag['rules']:
            trule = {'name': rule['rule'].name, 'id': rule['rule'].id, 'tag': ntag}
            if rule['choice'].has_key('current'):
                trule['current-state'] = rule['choice']['current'].state
                trule['current-value'] = rule['choice']['current'].value
            if rule['choice'].has_key('herited'):
                trule['herited-state'] = rule['choice']['herited'].state
                trule['herited-value'] = rule['choice']['herited'].value
            ret.append(trule)
    return json.dumps(ret)

#FIXME
from api.categories import get_conflevel
confuser, confcomputer = get_conflevel()
#print data_groups_tree(1)
#print data_categories_paned()
#print data_rules(confcomputer, 1, 2)


class Gaspacho(resource.Resource):
    isLeaf = True
    def getChild(self, name, request):
        if name == '':
            return self
        return Resource.getChild(self, name, request)

    def render_GET(self, request):
        if request.postpath[0] == 'data_categories_paned':
            return data_categories_paned()
        else:
            return "hu?"

    def render_POST(self, request):
        if request.postpath[0] == 'data_groups_tree':
            id = request.args['id'][0]
            if id == '':
                id = None
            else:
                id = int(id)
            return data_groups_tree(id)
        elif request.postpath[0] == 'data_rules':
            userid = request.args['userid'][0]
            groupid = int(request.args['groupid'][0])
            categoryid = int(request.args['categoryid'][0])
            if userid == '':
                userid = None
            else:
                userid = int(userid)
            return data_rules(categoryid, groupid, userid)
        elif request.postpath[0] == 'set_choice':
            userid = request.args['userid'][0]
            group = get_group_by_id(int(request.args['groupid'][0]))
            rule = get_rule_by_id(int(request.args['ruleid'][0]))
            state = unicode(request.args['state'][0])
            value = unicode(request.args['value'][0])
            if userid == '':
                user = None
            else:
                user = get_user_by_id(int(userid))
            choice = set_choice(rule=rule, group=group, user=user, state=state, value=value)
            session.commit()
            session.flush()
            return 'ok'
        else:
            return "hu?"

root = static.File("web/static/")
root.putChild("gaspacho", Gaspacho())
site = server.Site(root)
reactor.listenTCP(8080, site)
reactor.run()




# vim: ts=4 sw=4 expandtab
