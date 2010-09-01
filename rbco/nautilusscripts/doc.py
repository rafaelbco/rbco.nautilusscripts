from StringIO import StringIO
import util
import install

def get_title(title, title_char='-'):
    return '%s\n%s' % (title, len(title) * title_char) 

def get_doc_for_function(function):
    """Return the portion of the docstring of a script's function suitable for the README file."""
    return (getattr(function, '__doc__', None) or '').strip().split('\n')[0]
    
def get_scripts_readme():
    scripts = install.get_console_scripts_info()
        
    modules_functions = {}
    
    for s in scripts:
        modules_functions.setdefault(s['module'], []).append(s['function'])
    
    out = StringIO()
    
    for (module_name, function_names) in modules_functions.iteritems(): 
        module = __import__(module_name, fromlist=[0])
        
        print >> out, get_title(util.get_last_part_of_dotted_name(module_name))
        print >> out
        for function_name in function_names:
            function = getattr(module, function_name)
            doc = get_doc_for_function(function)
            out.write('- %s' % function_name)
            if doc:
                out.write(': %s' % doc)
            
            out.write('\n')        
            
        print >> out
    
    
    return out.getvalue()
    
