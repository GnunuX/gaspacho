# choices

from elixir import *

class Choice(Entity):
    state = Field(UnicodeText)
    value = Field(UnicodeText)
    rule = ManyToOne('Rule')
    group = ManyToOne('Group')
    user = ManyToOne('User')
    platform = ManyToOne('Platform')
    def __repr__(self):
        return 'state: "%s", value: "%s"' % (self.state, self.value)
	
# vim: ts=4 sw=4 expandtab
