#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Murilo Henrique Moreira'
SITENAME = 'Intricacy of Simplicity'
SITEURL = 'https://MuriloHMoreira.github.io/ios'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Define some project paths that have special meanings in Pelican
PATH = 'content'
ARTICLE_PATHS = ['blogs',]
PAGE_PATHS = ['pages']
PAGE_URL = '/{slug}/'
STATIC_PATHS = ['images', 'extra/main.css', 'extra/favicon.ico']

# Internationalization settings
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = 'en'


# Theme
THEME = "themes/pure-single"
COVER_IMG_URL = '/images/sidebar.svg'
TAGLINE = "Math, materials science, coding and whatever..."
SUMMARY_MAX_LENGTH = (20)
FAVICON = 'extra/FAVICON'
# Configure the site menu
# Fixed menu entries
MENUITEMS = (
    ('About this blog', '/ios/pages/about.html'),
    ('About me', 'https://murilohmoreira.github.io/'),
    ('Subscribe here!', '/ios/pages/subscribe.html'),
)

# Dynamic menu entries§
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False



# Gather as much metadata as possible from the file system
USE_FOLDER_AS_CATEGORY = True
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
DEFAULT_DATE = 'fs'
# Set some defaults§
DEFAULT_CATEGORY = 'ramblings'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_PAGINATION = 10


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_ALL_RSS = 'feeds/all.rss.xml'

# Social widget
SOCIAL = (('github', 'https://github.com/MuriloHMoreira'),
          ('orcid', 'https://orcid.org/0000-0002-2591-4760'),
          ('linkedin', 'https://www.linkedin.com/in/murilo-moreira-095534bb/'), 
          ('twitter', 'https://twitter.com/MuriloHMoreira'),
          ('rss', 'https://murilohmoreira.github.io/ios/feeds/all.rss.xml'),
                    )


MARKUP = ('md', 'ipynb')


# pelicanfly workaround
EXTRA_PATH_METADATA = {
    'extra/main.css': {'path': 'theme/css/main.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'pelicanfly']
DISQUS_SITENAME = "i-of-s"

# Give the control on the css highlighter
IPYNB_IGNORE_CSS=True

