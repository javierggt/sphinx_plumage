"""A theme for sphinx based on the plumage theme for pelican
"""

import setuptools
from distutils.core import setup

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='sphinx-plumage',  # Required
    version='0.1.0',  # Required
    description='A theme for sphinx based on the plumage theme for pelican',  # Required
    long_description=long_description,  # Optional

    url='https://github.com/javierggt/sphinx-plumage',  # Optional
    author='Javier G. Gonzalez',  # Optional
    author_email='javierggt@yahoo.com',  # Optional

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Framework :: Sphinx :: Theme',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='sphinx pelican theme',  # Optional
    packages=['sphinx_plumage'],

    entry_points={'sphinx.html_themes': ['plumage=sphinx_plumage']},

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    include_package_data=True,
    #package_data={'sphinx_plumage': []}

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('lib/python/site-packages/phys', ['phys/pdg_2017_elements.dat'])],  # Optional

    #project_urls={  # Optional
    #    'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
    #    'Funding': 'https://donate.pypi.org',
    #    'Say Thanks!': 'http://saythanks.io/to/example',
    #    'Source': 'https://github.com/pypa/sampleproject/',
    #},

    #install_requires=[],  # Optional

    #extras_require={  # Optional
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},
)
