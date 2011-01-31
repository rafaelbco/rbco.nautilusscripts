import os
import sys
import nautilus
import PyZenity  
from rbco.rename import renaming, console

__all__ = ['unhide', 'replace', 'mp3', 'lower_case_underscore', 'delete', 'delete_first_n_chars', 
    'add_suffix', 'add_prefix', 'remove_accentuation']

def unhide():
    files = nautilus.files

    for f in nautilus.files:
        renaming.unhide(f)

def replace():
    old = PyZenity.GetText('Enter the text to replace:')

    if old == None:
        sys.exit(1)

    new = PyZenity.GetText('Enter the new text:')

    if new == None:
        sys.exit(1)

    renaming.rename_replace(nautilus.paths, old, new)
    
def mp3():
    console.renmp3()    
    
def lower_case_underscore():
    console.renlu()    
    
def delete_first_n_chars():
    n = PyZenity.GetText('Enter the number of chars to delete:')

    if n != None:
        try:
            n = int(n)
        except ValueError:
            PyZenity.ErrorMessage('Invalid number of chars to delete.')
            sys.exit(1)
            
        renaming.rename_delete_first_chars(nautilus.paths, n)    
            
def delete():
    s = PyZenity.GetText('Enter the text to delete:')

    if s != None:
        renaming.rename_replace(nautilus.paths, s, '')
        
def add_suffix():
    suffix = PyZenity.GetText('Enter the suffix:')

    if suffix != None:
        preserveExtension = PyZenity.Question('Preserve file extension ?')
        renaming.rename_suffix(nautilus.paths, suffix, preserveExtension)        
        
def add_prefix():
    prefix = PyZenity.GetText('Enter the prefix:')

    if prefix != None:
        renaming.rename_prefix(nautilus.paths, prefix)            
        
def remove_accentuation():
    console.renremoveacc()
