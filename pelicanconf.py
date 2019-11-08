#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'John Manalastas'
SITENAME = "All Things Data"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/jaymanalastas'),
          ('email', 'jay.manalastas@outlook.com'),
	  ('facebook','https://www.facebook.com/johnjay.manalastas'),
          ('linkedin', 'https://www.linkedin.com/in/jaymanalastas/'),)


AUTHORS_BIO = {
  "John Manalastas": {
    "name": "John Manalastas",
    "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    "LinkedIn": "https://www.linkedin.com/in/jaymanalastas/",
    "location": "Orlando, FL",
    "bio": "Analyst looking to leverage my passion for learning and analyzing trends to produce actionable analysis to executives."
  }
}


PROFILE_IMAGE = "img/PROFILE.jpg"
GITHUB_URL = ('https://github.com/jaymanalastas')
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

COLOR_SCHEME_CSS = 'monokai.css'

STATIC_PATHS = ['2019']

RELATIVE_URLS = False

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = "themes/attila"
