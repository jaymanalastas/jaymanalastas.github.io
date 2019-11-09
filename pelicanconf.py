#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'John Manalastas'
SITENAME = u"Data Like You Mean It"
SITESUBTITLE = u'Blogging my way into data science'
SITEURL = ''

PATH = 'content'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Pagination: 
DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

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

# PROFILE_IMAGE = "img/PROFILE.jpg"
GITHUB_URL = ('https://github.com/jaymanalastas')
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
HOME_COLOR = 'black'
#COLOR_SCHEME_CSS = 'darkly.css'
STATIC_PATHS = ['assets']

EXTRA_PATH_METADATA = {
    'assets/robots.txt': {'path': 'robots.txt'},
    'assets/favicon.ico': {'path': 'favicon.ico'},
    'assets/CNAME': {'path': 'CNAME'}
}



## Post and Pages Path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'



##ignore file 
IGNORE_FILES = ['.ipynb_checkpoints']


## Tags and Category path:
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'



RELATIVE_URLS = False
MARKUP = ('md', 'ipynb')



#### Plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['sitemap', 'neighbors','ipynb.markup','assets','static_comments']
#'ipynb.markup', 'assets', 
### Stiemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

THEME = "themes/attila"


####
# To set background image for the home page.
HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'
#'https://casper.ghost.org/v1.0.0/images/welcome.jpg'


# Custom Header

HEADER_COVERS_BY_TAG = {'python':'https://casper.ghost.org/v1.0.0/images/writing.jpg','data':'https://www.freeimages.com/photo/dhow-1517243'}

AUTHORS_BIO = {
  "john manalastas": {
    "name": "John Manalastas",
   # "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
    "image": "https://casper.ghost.org/v1.0.0/images/writing.jpg",
    "linkedin": "jaymanalastas/",
    "github": "jaymanalastas",
    "location": "Orlando, FL",
    "bio": "Finance leader looking to leverage my passion for learning and analyzing trends to produce actionable analysis to executives."

  }
}

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['assets/css/myblog.css']

# Jinja config - Pelican 4
JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.with_',
    'jinja2.ext.do'
  ]
}

JINJA_FILTERS = {'max': max}

