import nautilus
from . import PyZenity
from rbco.rename import renaming
import util
from docutils.core import publish_file
from .wrapper import nautilus_script

@nautilus_script
def rst2html():
    if len(nautilus.files) != 1:
        PyZenity.ErrorMessage('Exactly one file must be selected.')
    
    input_filename = nautilus.files[0]
    output_filename = renaming.removeExtension(input_filename) + '.html'
    
    util.call_no_exit(
        publish_file, 
        writer_name='html', 
        source_path=input_filename, 
        destination_path=output_filename
    )
            
        
    
