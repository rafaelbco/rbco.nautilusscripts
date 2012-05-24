import nautilus
import os.path
from . import PyZenity
from .wrapper import nautilus_script

@nautilus_script
def filename_length():
    PyZenity.InfoMessage("File name length is %d." % len(nautilus.files[0]))

@nautilus_script
def real_path():
    PyZenity.GetText('File path is:', os.path.realpath(nautilus.paths[0]))    
