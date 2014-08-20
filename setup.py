from setuptools import setup, find_packages

version = '0.8'


def get_console_script_entry_point(function, module):
    return 'nautilus_%(module)s_%(function)s = rbco.nautilusscripts.%(module)s:%(function)s' % {
        'module': module,
        'function': function
    }

setup(name='rbco.nautilusscripts',
      version=version,
      description="A set of scripts for Nautilus, the Gnome file manager application.",
      long_description=open("README.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='linux gnome',
      author='Rafael Oliveira',
      author_email='rafaelbco@gmail.com',
      url='',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['rbco'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'clom',
          'rbco.rename>=0.5',
      ],
      entry_points={
          'console_scripts': [
              get_console_script_entry_point('open_real_path', 'misc'),
              get_console_script_entry_point('open_in_terminal', 'misc'),
              get_console_script_entry_point('change_owner_to_me', 'misc'),
              get_console_script_entry_point('backup', 'misc'),
              get_console_script_entry_point('execute_custom_command', 'misc'),

              get_console_script_entry_point('filename_length', 'fileinfo'),
              get_console_script_entry_point('real_path', 'fileinfo'),

              get_console_script_entry_point('lower_case_underscore', 'rename'),
              get_console_script_entry_point('unhide', 'rename'),
              get_console_script_entry_point('add_prefix', 'rename'),
              get_console_script_entry_point('delete_first_n_chars', 'rename'),
              get_console_script_entry_point('replace', 'rename'),
              get_console_script_entry_point('mp3', 'rename'),
              get_console_script_entry_point('id3', 'rename'),
              get_console_script_entry_point('add_suffix', 'rename'),
              get_console_script_entry_point('delete', 'rename'),
              get_console_script_entry_point('remove_accentuation', 'rename'),

              get_console_script_entry_point('rst2html', 'text'),

              'rbco_nautilusscripts_install = rbco.nautilusscripts.install:install'
          ],
      },
)
