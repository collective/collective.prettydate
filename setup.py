# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.2.3.dev0'
description = "Fuzzy dates for Plone."
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(name='collective.prettydate',
      version=version,
      description=description,
      long_description=long_description,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          "Framework :: Plone :: 5.0",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Topic :: Office/Business :: News/Diary",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='plone fuzzy date datetime',
      author='Franco Pellegrini',
      author_email='frapell@gmail.com',
      url='https://github.com/collective/collective.prettydate',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.i18nmessageid',
          'zope.interface',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'unittest2',
              'zope.component',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
