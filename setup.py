from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='rbco.nautilusscripts',
      version=version,
      description="A set of scripts for Nautilus, the Gnome file manager application.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
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
          'rbco.rename>=0.2',
          'PyZenity',
      ],
      entry_points={
          'console_scripts': [
              'open_real_path = rbco.nautilusscripts.misc:open_real_path',
              'open_in_terminal = rbco.nautilusscripts.misc:open_in_terminal',              
              'change_owner_to_me = rbco.nautilusscripts.misc:change_owner_to_me',              
              'backup = rbco.nautilusscripts.misc:backup',              

              'filename_length = rbco.nautilusscripts.fileinfo:filename_length',              
              'real_path = rbco.nautilusscripts.fileinfo:real_path',              

              'lower_case_underscore = rbco.nautilusscripts.rename:lower_case_underscore',
              'unhide = rbco.nautilusscripts.rename:unhide',              
              'add_prefix = rbco.nautilusscripts.rename:add_prefix',              
              'delete_first_n_chars = rbco.nautilusscripts.rename:delete_first_n_chars',              
              'replace = rbco.nautilusscripts.rename:replace',              
              'mp3 = rbco.nautilusscripts.rename:mp3',              
              'add_suffix = rbco.nautilusscripts.rename:add_suffix',          
              'delete = rbco.nautilusscripts.rename:delete',                                                                                                                                                                                                        
          ],
      },
)
