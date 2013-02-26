"""Provide the `install` function"""
import sys
import os
import misc, fileinfo, rename
import util
import pkg_resources


def get_new_script_path(module_name, function_name):
    """
    Given a `module_name` name and a `function_name` return the path where to install the
    correspondent script. The path is relative to "~/.gnome2/nautilus-scripts".
    """
    return os.path.join(util.get_last_part_of_dotted_name(module_name), function_name)


def get_console_scripts_info():
    """
    Return a sequence of dicts, one for each console scripts installed by this package,
    containing the following keys:
    - name: The script name.
    - module: The module name.
    - function: The function name.

    Note: exclude the install script.
    """
    entry_points_map = pkg_resources.get_entry_map('rbco.nautilusscripts', 'console_scripts')
    return [
        {
            'name': ep.name,
            'module': ep.module_name,
            'function': ep.attrs[0],
        }
        for ep in entry_points_map.itervalues()
        if not ep.module_name.endswith('.install')
    ]


def link_scripts(dest_dir):
    original_scripts_dir = util.get_installed_scripts_dir()

    scripts = [
        (s['name'], get_new_script_path(s['module'], s['function']))
        for s in get_console_scripts_info()
    ]

    for (original, new_path) in scripts:
        original_path = os.path.join(original_scripts_dir, original)
        new_path = os.path.join(dest_dir, new_path)

        util.mkdir_p(os.path.dirname(new_path))

        print 'Symlinking %s to %s ...' % (original_path, new_path)
        if os.path.exists(new_path):
            os.remove(new_path)
        os.symlink(original_path, new_path)


def install():
    """Install the Nautilus' scripts for the current user."""
    print 'Creating links for Nautilus ...'
    dest = os.path.expanduser('~/.gnome2/nautilus-scripts')
    link_scripts(dest)
    print
    print 'Creating links for Nemo ...'
    dest = os.path.expanduser('~/.gnome2/nemo-scripts')
    link_scripts(dest)
