from StringIO import StringIO
import install
import util

def get_title(title, title_char='-'):
    return '%s\n%s' % (title, len(title) * title_char) 

def get_doc_for_function(function):
    """Return the portion of the docstring of a script's function suitable for the README file."""
    return (getattr(function, '__doc__', None) or '').strip().split('\n')[0]

def get_module_readme(module):
    out = StringIO()
    print >> out, get_title(util.get_last_part_of_dotted_name(module.__name__))
    print >> out
    for function_name in module.__all__:
        function = getattr(module, function_name)
        doc = get_doc_for_function(function)
        out.write('- %s' % function_name)
        if doc:
            out.write(': %s' % doc)
        
        out.write('\n')
        
    
    return out.getvalue()
    
def get_readme():
    return '\n'.join(get_module_readme(m) for m in install.MODULES)
    
