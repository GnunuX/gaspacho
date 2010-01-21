"""
wrapper
"""

# ____________________________________________________________
# Wrapped objects
 
class APIWrapper:
    def __init__(self, wrap):
        self._w = wrap

    def __getattr__(self, name):
        return getattr(self._w, name)
    
    def get_w(self, name):
        return getattr(self._w, name)
    def set_w(self, name, value):
        return setattr(self._w, name, value)
    
    _w = property (get_w, set_w)
 
 
