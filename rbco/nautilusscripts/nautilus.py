"""Nautilus scripts utilities."""
import os
import os.path
import sys
import urllib

def file_uri_to_path(uri):
    """
    Converts a file uri to a path.

    Eg.: if uri is "file:///home/rafaelb" then "/home/rafaelb" is returned.
    """
    if not uri.startswith("file://"):
        return uri

    return urllib.unquote(uri.replace('file://', '', 1))


_programs = ('NAUTILUS', 'NEMO', 'CAJA')
_possible_names = ['{0}_SCRIPT_CURRENT_URI'.format(i) for i in _programs]
_var_name = [i for i in _possible_names if i in os.environ]

current_uri_var_name = _var_name[0] if _var_name else _programs[0]

current_uri = os.environ.get(current_uri_var_name, '')
current_path = file_uri_to_path(current_uri)
"""Current absolute path."""

files = sys.argv[1:]
"""Selected file names."""

paths = [os.path.join(current_path, f) for f in files]
"""Sequence containing the absolute paths for the selected files."""
