import os
import pwd
import grp
from distutils.command.install import install as Install
from distutils.dist import Distribution
import sys

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
        
def get_installed_scripts_dir():
    """
    Return the absolute path to the directory where scripts created by easy_install are located.
    This is usually "/usr/bin" or "/usr/local/bin".
    """
    i = Install(Distribution())
    i.finalize_options()
    return i.install_scripts       
    
def call_no_exit(f, *args, **kwargs):
    """Call `f` with the given arguments but preventing the call of sys.exit."""
    old_exit = sys.exit
    def new_exit(*args, **kwargs):
        pass
        
    sys.exit = new_exit    
    retval = f(*args, **kwargs)
    sys.exit = old_exit
    
    return retval     
