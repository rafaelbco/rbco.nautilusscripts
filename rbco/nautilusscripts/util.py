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
