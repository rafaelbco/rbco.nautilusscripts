from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='rbco.nautilusscripts',
      version=version,
      description="A set of scripts for Gnome's Nautilus.",
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
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
