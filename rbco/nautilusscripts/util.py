import os
import pwd
import grp

def get_last_part_of_dotted_name(name):
    return name.split('.')[-1]

def escape_space(s):
    return s.replace(' ', '\ ')
    
def user_main_group(userid):
    """Return the name of the main group which the given user belongs to."""
    return grp.getgrgid(pwd.getpwnam(userid)[3])[0]    
    
    
def gksu(cmd):
    """Run the given command using gksu."""    
    gksu_cmd = 'gksu "%s"' % cmd
    os.system(gksu_cmd)    
    
def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)    
        
def get_original_script_name(module_name, function_name):
    """
    Given a `module_name` name and a `function_name` return the name of the executable script
    created in this package's setup.py. 
    
    The returned name is resolved using the same naming schema as in setup.py. The naming schema
    must be kept in sync in these two places.
    """
    return 'nautilus_%s_%s' % (util.get_last_part_of_dotted_name(module_name), function_name)        
