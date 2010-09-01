"""Provide the `install` function"""
import sys
import os
import misc, fileinfo, rename
import util

MODULES = [misc, fileinfo, rename]

def get_new_script_path(module_name, function_name):
    """
    Given a `module_name` name and a `function_name` return the path where to install the correspondent
    script. The path is relative to "~/.gnome2/nautilus-scripts".
    """
    return os.path.join(util.get_last_part_of_dotted_name(module_name), function_name)

def install():
    """Install the Nautilus' scripts for the current user."""
    
    original_scripts_dir = os.path.join(sys.prefix, 'bin')
    nautilus_scripts_dir = os.path.expanduser('~/.gnome2/nautilus-scripts')    
        
    scripts = []     
    for m in MODULES:
        scripts.extend(
            (util.get_original_script_name(m.__name__, f), get_new_script_path(m.__name__, f))
            for f in m.__all__
        )
    
    for (original, new_path) in scripts:
        original_path = os.path.join(original_scripts_dir, original)
        new_path = os.path.join(nautilus_scripts_dir, new_path)
        
        util.mkdir_p(os.path.dirname(new_path))
        
        print 'Symlinking %s to %s ...' % (original_path, new_path)
        
        os.symlink(original_path, new_path)
    
    
    
