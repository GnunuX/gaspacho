from xml.etree import ElementTree as ET

FILE = "ListeRegles.xml"

class Software():
    confuser = None
    confcomputer = None
    def __init__(self, name):
        self.name=name

class Confuser():
    def __init__(self, rules):
        self.rules = rules

class Confcomputer():
    def __init__(self, rules):
        self.rules = rules

class Rule():
    classobject = None
    typ = None
    os = None
    regle = None
    path = None
    variable = None
    vartyp = None
    valueon = None
    valueoff = None
    comment = None

class Tag():
    rules = None
    def __init__(self, name):
        self.name=name

class Category():
    tags = None
    def __init__(self, name):
        self.name=name

def parse_software(soft):
    attrib = soft.attrib
    return Software(attrib['nom'])

def parse_var(var):
    attrib = var.attrib
    variable = attrib['nom']
    vartyp = attrib['type']
    valueon = var.find('ValueOn')
    valueoff = var.find('ValueOff')
    return (variable, vartyp, valueon, valueoff)


def parse_conf(confs):
    for conf in confs.findall('Regle'):
        regle = Regle()
        attrib = conf.attrib
        if attrib.has_key('classeobjet'):
            regle.classobject = attrib['classeobjet']
        regle.typ = attrib['type']
        regle.os = conf.find('OS').text
        regle.path = conf.find('Chemin').text
        regle.variable, regle.vartyp, regle.valueon, regle.valueoff = parse_var(conf.find('Variable'))
        regle.comment = conf.find('Commentaire').text
        yield regle

def parse_tag(tags):
    for tag in tags.findall('OU'):
        attrib = tag.attrib
        if attrib.classeobjet != "BlocRegle":
            print "rehu? " + attrib.classeobjet
        otag = Tag(attrib.nom)
        otag.rules = list(parse_conf(tag))
        yield otag

def parse_category(cats):
    try:
        for cat in cats.findall('OU'):
            attrib = cat.attrib
            if attrib.classeobjet != "Categorie":
                print "hu? " + attrib.classeobjet
            ocat = Category(attrib.nom)
            ocat.tags = list(parse_tag(cat.findall('OU')))
            yield ocat
    except:
        ocat = Category("no cat")
        ocat.tags = Tag("no tag")
        ocat.tags.rules = list(parse_conf(cats))
        yield ocat


tree = ET.ElementTree()
tree.parse(FILE)
#tree = tree.find('AppRef')
tree = tree.find('ListeRegles')
ret = []
for var in tree.findall('Application'):
    soft = parse_software(var)
    cat = var.find('ConfUtilisateur')
    soft.confuser = Confuser(list(parse_category(cat)))
    conf = var.find('ConfMachine')
    soft.confcomputer = Confcomputer(list(parse_category(cat)))
    ret.append(soft)

print ret


# vim: ts=4 sw=4 expandtab
