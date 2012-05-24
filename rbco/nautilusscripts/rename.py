import os
import sys
import nautilus
from . import PyZenity  
from rbco.rename import renaming, console
from .wrapper import nautilus_script

@nautilus_script
def unhide():
    files = nautilus.files

    for f in nautilus.files:
        renaming.unhide(f)

@nautilus_script
def replace():
    old = PyZenity.GetText('Enter the text to replace:')

    if old == None:
        sys.exit(1)

    new = PyZenity.GetText('Enter the new text:')

    if new == None:
        sys.exit(1)

    renaming.rename_replace(nautilus.paths, old, new)
    
@nautilus_script    
def mp3():
    console.renmp3()    

@nautilus_script
def id3():
    console.renid3()    
    
@nautilus_script    
def lower_case_underscore():
    console.renlu()    
    
@nautilus_script    
def delete_first_n_chars():
    n = PyZenity.GetText('Enter the number of chars to delete:')

    if n != None:
        try:
            n = int(n)
        except ValueError:
            PyZenity.ErrorMessage('Invalid number of chars to delete.')
            sys.exit(1)
            
        renaming.rename_delete_first_chars(nautilus.paths, n)    
            
@nautilus_script            
def delete():
    s = PyZenity.GetText('Enter the text to delete:')

    if s != None:
        renaming.rename_replace(nautilus.paths, s, '')

@nautilus_script        
def add_suffix():
    suffix = PyZenity.GetText('Enter the suffix:')

    if suffix != None:
        preserveExtension = PyZenity.Question('Preserve file extension ?')
        renaming.rename_suffix(nautilus.paths, suffix, preserveExtension)        
        
@nautilus_script        
def add_prefix():
    prefix = PyZenity.GetText('Enter the prefix:')

    if prefix != None:
        renaming.rename_prefix(nautilus.paths, prefix)            
        
@nautilus_script        
def remove_accentuation():
    console.renremoveacc()
