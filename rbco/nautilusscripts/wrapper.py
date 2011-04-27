import PyZenity

def capture_exceptions(f):
    """Decorator which captures any exception and display it using PyZenity."""
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)            
        except Exception, e:
            PyZenity.ErrorMessage(str(e))
        
    return wrapped
