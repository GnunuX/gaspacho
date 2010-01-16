# choices

from elixir import *

class Choice(Entity):
    rule = ManyToOne('Rule')
    group = ManyToOne('Group')
    user = ManyToOne('User')
    state = Field(UnicodeText)
    value = Field(UnicodeText)
    platform = ManyToOne('Platform')
    def __repr__(self):
        return 'state: "%s", value: "%s"' % (self.state, self.value)
	
# vim: ts=4 sw=4 expandtab
