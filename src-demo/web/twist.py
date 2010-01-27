from twisted.web import server, resource, static, server
from twisted.internet import reactor
from  web.test import data_groups_tree

class Gaspacho(resource.Resource):
    isLeaf = True
    def getChild(self, name, request):
        if name == '':
            return self
        return Resource.getChild(self, name, request)

    def render_GET(self, request):
        test = """<form id="formword" method="post" action="data_groups_tree">
	<input type="text" id="textword" name="id"/>
	<input type="submit" value="Envoyer" id="test"/>
	</form>"""
	return test

    def render_POST(self, request):
        if request.postpath[0] == 'data_groups_tree':
            return data_groups_tree(int(request.args['id'][0]))
        else:
            return "hu?"

root = static.File("web/static/")
root.putChild("gaspacho", Gaspacho())
site = server.Site(root)
reactor.listenTCP(8080, site)
reactor.run()

