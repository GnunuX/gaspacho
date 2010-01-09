# choices

from elixir import *

class Choice(Entity):
    rule = ManyToOne('Rule')
    group = ManyToOne('Group')
    user = ManyToOne('User')
    state = Field(UnicodeText)
    value = Field(UnicodeText)
	
# vim: ts=4 sw=4 expandtab
