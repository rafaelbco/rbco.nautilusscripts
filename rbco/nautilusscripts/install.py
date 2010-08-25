import sys
import os
from rbco.nautilusscripts import misc, fileinfo, rename

def get_original_script_name(module, function):
    return 'nautilus_%s_%s' % (module.split('.')[-1], function)

def get_new_script_path(module, function):
    return os.path.join(module.split('.')[-1], function)

def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)

def install():
    """Install the Nautilus' scripts for the current user."""
    original_scripts_dir = os.path.join(sys.prefix, 'bin')
    nautilus_scripts_dir = os.path.expanduser('~/.gnome2/nautilus-scripts')
    
    modules = [misc, fileinfo, rename]
        
    scripts = []     
    for m in modules:
        scripts.extend(
            (get_original_script_name(m.__name__, f), get_new_script_path(m.__name__, f))
            for f in m.__all__
        )
    
    for (original, new_path) in scripts:
        original_path = os.path.join(original_scripts_dir, original)
        new_path = os.path.join(nautilus_scripts_dir, new_path)
        
        mkdir_p(os.path.dirname(new_path))
        
        print 'Symlinking %s to %s ...' % (original_path, new_path)
        
        os.symlink(original_path, new_path)
    
    
    
