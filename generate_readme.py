"""
Generate README.txt using README.txt.in as a template and filling information from the ``doc``
module and HISTORY.txt
"""
from rbco.nautilusscripts import doc
import os

if __name__ == '__main__':
    readme = open('README.txt.in').read() % {
        'scripts_info': doc.get_scripts_readme(),
        'history': open(os.path.join('docs', 'HISTORY.txt')).read()
    }
    
    f = open('README.txt', 'w')
    f.write(readme)
    f.close()


if False:
    print 'a'



def a():
    pass




