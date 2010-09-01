from rbco.nautilusscripts import doc
import os

if __name__ == '__main__':
    print open('README.txt.in').read() % {
        'scripts_info': doc.get_readme(),
        'history': open(os.path.join('docs', 'HISTORY.txt')).read()
    }
