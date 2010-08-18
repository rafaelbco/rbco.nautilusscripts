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

current_path = file_uri_to_path(os.environ.get('NAUTILUS_SCRIPT_CURRENT_URI', ''))
"""Current absolute path."""

files = sys.argv[1:]
"""Selected file names."""
      
paths = [os.path.join(current_path, f) for f in files]
"""Sequence containing the absolute paths for the selected files."""
