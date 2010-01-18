# _*_ coding: iso-8859-1 _*_
import sys 

#if __name__ == '__main__':

from elixir import *
from api.rules import add_rule, add_variable
from api.platforms import add_platform, add_path, add_os, add_software
from api.tags import add_tag, add_category, get_conflevel
from bdd.tags import ConfLevel
from api.groups import add_group, add_template, add_user, add_computer
from api.choices import add_choice

metadata.bind = "sqlite:///gaspacho.sqlite"
setup_all()
create_all()

confuser, confcomputer = get_conflevel()

#------------------------------------------------------------------------------
# I - OS and Software

win = add_os(name=u'windows')
winxp = win.add_version(u'XP')

mdv = add_os(name=u'mandriva')
mdv20100 = mdv.add_version(name=u'2010.0')

gdm = add_software(name=u'gdm')
gdm2 = gdm.add_version(name=u'2.20.10')

firefox = add_software(name=u'firefox')
f35 = firefox.add_version(name=u'3.5')

ie = add_software(name=u'ie')
ie6 = ie.add_version(name=u'6.0')
ie7 = ie.add_version(name=u'7.0')

#------------------------------------------------------------------------------
# II - Category and tag

cat_navweb = add_category(name=u'Navigateur web')
tag_actproxy = add_tag(name=u'Activer le Proxy')
tag_conf = add_tag(name=u'Configuration')
cat_navweb.add_tag(tag_actproxy)
cat_navweb.add_tag(tag_conf)

cat_session = add_category(name=u'Session')
tag_ouvsess = add_tag(name=u'Ouverture de session')
cat_session.add_tag(tag_ouvsess)

#------------------------------------------------------------------------------
# III - Rule

# 1/ Premiere regle :
rulea = add_rule(name=u"Autoriser l'arrêt de la machine depuis la fenêtre d'ouverture de session", typ=u'boolean', comment=u'', defaultvalue=u'3128') 

rulea.set_tag(tag_ouvsess)
rulea.set_conflevel(confcomputer)

# sous mandriva / gdm
variableA = add_variable(name=u'AllowLogoutActions', comment=u'', valueon=u'HALT;REBOOT;SUSPEND;CUSTOM_CMD', valueoff=u'CUSTOM_CMD', typ=u'string')
path_gdm2 = add_path(name=u'INI://etc/X11/gdm/custom.conf?section=daemon')
gdm2onmdv10 = add_platform(mdv20100, gdm2, path_gdm2)

rulea.add_variable(variableA)
variableA.set_platform(platform=gdm2onmdv10)

# sous windows XP
variableB = add_variable(name=u'ShutdownWithoutLogon', comment=u'', valueon=u'', valueoff=u'', typ=u'integer')
path_session = add_path(name=u'REG://HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\policies\\System')
sessiononwixp = add_platform(winXP, path=path_session)

rulea.add_variable(variableB)
variableB.set_platform(platform=sessiononwixp)

#------------------------------------------------------------------------------
# IV - User

student = add_user(name=u'student', typ=u'group')
teacher = add_user(name=u'teacher', typ=u'group')
fred = add_user(name=u'fred')
paul = add_user(name=u'paul')

#------------------------------------------------------------------------------
# V - Computer

allcomputers = add_computer(name=u'*')
roomcomputers = add_computer(name=u'*room*', typ=u'name')
mathcomputers = add_computer(name=u'mathroom*', typ=u'name')
techcomputers = add_computer(name=u'techroom*', typ=u'name')

#------------------------------------------------------------------------------
# VI - Group

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

tplfirefox = add_template(name=u'tplfirefox')
tplfirefox.add_software(firefox)
mathroom.add_depend(tplfirefox)

#------------------------------------------------------------------------------
# VII - Choice

#choicea = add_choice(rule=rulea, group=mathroom, state=u'on', value=u'3120')
#choicea = add_choice(rule=rulea, group=mathroom, state=u'on', value=u'3118', platform=f35onWinXP)
#choicea = add_choice(rule=rulea, group=room, state=u'on', value=u'3119')
#choicea = add_choice(rule=rulea, template=tplfirefox, state=u'on', value=u'3119')

#----
session.commit()
session.flush()
# vim: ts=4 sw=4 expandtab
