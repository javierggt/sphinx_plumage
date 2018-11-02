Sphinx+Plumage
==============

Plumage is a theme for [Pelican](https://getpelican.com), a static site
generator written in Python written by [Kevin Deldycke](https://kevin.deldycke.com)

This is a theme for [Sphinx](http://www.sphinx-doc.org) that uses the same stylesheets.
It does not have all the features in Plumage, because this is only intended for Sphinx.

To install, one can do the following:

 pip install -e git+https://github.com/javierggt/sphinx-plumage

I added the following to my sphinx configuration, conf.py:

 html_theme = 'plumage'
 html_theme_options = {
     'site_thumbnail': 'muon_thumb.png',
     'site_thumbnail_text': 'LDF',
     #'header_links':[('Title', 'url', 'description')]
 }
