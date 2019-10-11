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

BIO = "Analyst looking to leverage my passion for learning and analyzing trends to produce actionable analysis to executives."

PROFILE_IMAGE = "PROFILE.jpg"

GITHUB_URL = ('https://github,com/jaymanalastas')
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
STATIC_PATH = ['2019/img']

RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

THEME = "themes/pelican-hyde"
