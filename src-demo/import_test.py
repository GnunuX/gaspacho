# _*_ coding: iso-8859-1 _*_
import sys 

#if __name__ == '__main__':

from elixir import *
from api.rules import add_rule
from api.platforms import add_platform, add_path, add_os, add_software
from api.tags import add_tag, add_category, get_conflevel
from bdd.tags import ConfLevel
from api.groups import add_group, add_user, add_computer
from api.choices import add_choice

metadata.bind = "sqlite:///gaspacho.sqlite"
setup_all()
create_all()

confuser, confcomputer = get_conflevel()

##--Platform
win = add_os(name=u'windows')
winxp = win.add_version(u'XP')
winpath = add_path(name=u'ini://path/to/app1/Win/')
#
mdv = add_os(name=u'mandriva')
mdv20100 = mdv.add_version(name=u'2010.0')
mdvpath = add_path(name=u'ini://path/to/app1/Lin/')
#
firefox = add_software(name=u'firefox')
f35 = firefox.add_version(name=u'3.5')
#
ie = add_software(name=u'ie')
ie6 = ie.add_version(name=u'6.0')
#
f35onWinXP = add_platform(winxp, f35, winpath)
ieonWinXP = add_platform(winxp, ie6, winpath)
f35onMdv20100 = add_platform(mdv20100, f35, mdvpath)
#

student = add_user(name=u'student', typ=u'group')
teacher = add_user(name=u'teacher', typ=u'group')
fred = add_user(name=u'fred')
paul = add_user(name=u'paul')

allcomputers = add_computer(name=u'*')
roomcomputers = add_computer(name=u'*room*', typ=u'name')
mathcomputers = add_computer(name=u'mathroom*', typ=u'name')
techcomputers = add_computer(name=u'techroom*', typ=u'name')

defaultgroup = add_group(name=u'default')
defaultgroup.add_user(student)
defaultgroup.add_user(teacher)
defaultgroup.add_manager(paul)
defaultgroup.add_computer(allcomputers)

room = add_group(name=u'room', parent=defaultgroup)
room.add_user(student)
room.add_user(teacher)
room.add_computer(roomcomputers)

mathroom = add_group(name=u'mathroom', parent=room)
mathroom.add_user(student)
mathroom.add_user(teacher)
mathroom.add_manager(fred)
mathroom.add_computer(mathcomputers)

techroom = add_group(name=u'techroom', parent=room)
techroom.add_user(student)
techroom.add_user(teacher)
techroom.add_computer(techcomputers)

tplfirefox = add_group(name=u'tplfirefox', template=True)
tplfirefox.add_software(firefox)
mathroom.add_depend(tplfirefox)

#----
tag1 = add_tag(name=u'proxy')
tag2 = add_tag(name=u'default')

category1 = add_category(name=u'web browser')
#----
rulea = add_rule(name=u'configure proxy port', typ=u'integer', comment=u'', defaultvalue=u'3128') 
rulea.set_tag(tag1)
rulea.set_category(category1)
rulea.set_conflevel(confuser)
#--
ruleb = add_rule(name=u'configure proxy address', typ=u'string', comment=u'')
ruleb.set_tag(tag1)
ruleb.set_category(category1)
ruleb.set_conflevel(confuser)
#--
rulec = add_rule(name=u'configure app1 as default', typ=u'boolean', comment=u'', defaultstate=u'on')
rulec.set_tag(tag2)
rulec.set_category(category1)
rulec.set_conflevel(confuser)
#--
ruled = add_rule(name=u'configure app3 as default', typ=u'boolean', comment=u'', defaultstate=u'on')
ruled.set_tag(tag2)
ruled.set_category(category1)
ruled.set_conflevel(confcomputer)
#--
rulee = add_rule(name=u'configure app4 as default', typ=u'boolean', comment=u'')
rulee.set_tag(tag2)
rulee.set_category(category1)
rulee.set_conflevel(confcomputer)
#--
rulef = add_rule(name=u'configure app5 as default', typ=u'boolean', comment=u'')
rulef.set_tag(tag2)
rulef.set_category(category1)
rulef.set_conflevel(confcomputer)
#--
#----

variableA = rulea.add_variable(name=u'proxy_port', comment=u'', valueon=u'', valueoff=u'SUPPR', typ=u'integer')
path01 = variableA.set_platform(platform=f35onWinXP)
path06 = variableA.set_platform(platform=ieonWinXP)

#--
variableB = ruleb.add_variable(name=u'proxy_addr', comment=u'', valueon=u'', valueoff=u'SUPPR', typ=u'string')
path02 = variableB.set_platform(platform=f35onWinXP)
#--
variableC = rulec.add_variable(name=u'default', comment=u'', valueon=u'on', valueoff=u'SUPPR', typ=u'string')
path03 = variableC.set_platform(platform=f35onWinXP)
path04 = variableC.set_platform(platform=f35onMdv20100)
path05 = variableC.set_platform(platform=ieonWinXP)
variableG = rulea.add_variable(name=u'proxyport', comment=u'', valueon=u'', valueoff=u'SUPPR', typ=u'integer')
path10 = variableG.set_platform(platform=f35onMdv20100)
#--
variableH = ruleb.add_variable(name=u'proxyaddr', comment=u'', valueon=u'', valueoff=u'SUPPR', typ=u'string')
path11 = variableH.set_platform(platform=f35onMdv20100) 
#--
variableI = ruled.add_variable(name=u'default', comment=u'', valueon=u'0', valueoff=u'1', typ=u'boolean')
path12 = variableI.set_platform(platform=f35onWinXP)
#--
variableJ = rulea.add_variable(name=u'proxyport', comment=u'', valueon=u'', valueoff=u'SUPPR', typ=u'integer')
path13 = variableJ.set_platform(platform=f35onMdv20100) 
#--
variableK = ruleb.add_variable(name=u'proxyaddr', comment=u'', valueon=u'', valueoff=u'SUPPR', typ=u'string')
path14 = variableK.set_platform(platform=f35onWinXP)
#--
variableL = rulee.add_variable(name=u'default1', comment=u'', valueon=u'SUPPR', valueoff=u'off', typ=u'string')
path15 = variableL.set_platform(platform=ieonWinXP) 
#--
variableM = rulef.add_variable(name=u'default2', comment=u'', valueon=u'0', valueoff=u'SUPPR', typ=u'boolean')
path16 = variableM.set_platform(platform=f35onMdv20100)
path17 = variableM.set_platform(platform=f35onWinXP)
#----
choicea = add_choice(rule=rulea, group=mathroom, state=u'on', value=u'3120')
choicea = add_choice(rule=rulea, group=mathroom, state=u'on', value=u'3118', platform=f35onWinXP)
#choicea = add_choice(rule=rulea, group=room, state=u'on', value=u'3119')
choicea = add_choice(rule=rulea, group=tplfirefox, state=u'on', value=u'3119')
#----
session.commit()
session.flush()
# vim: ts=4 sw=4 expandtab
