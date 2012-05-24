from . import PyZenity
from functools import wraps

def capture_exceptions(f):
    """Decorator which captures any exception and display it using PyZenity."""
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)            
        except Exception, e:
            PyZenity.ErrorMessage(str(e))
        
    return wrapped

def nautilus_script(f):
    """Functions implementing the entry points for Nautilus scripts must use this decorator."""
    return capture_exceptions(f)