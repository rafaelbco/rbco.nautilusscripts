import nautilus
import os.path
import PyZenity

__all__ = ['filename_length', 'real_path']

def filename_length():
    PyZenity.InfoMessage("File name length is %d." % len(nautilus.files[0]))
    
def real_path():
    PyZenity.GetText('File path is:', os.path.realpath(nautilus.paths[0]))    
