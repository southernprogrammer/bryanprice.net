#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bryan Price'
SITENAME = u'Bryan Price'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

THEME = '../pelican-themes/blueidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Joshua Rogers', 'http://joshuarogers.net'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/southrnprogrmmr'),('Github', 'https://github.com/southernprogrammer'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['youtube']

# Theme Variables

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SUBMENU = True
DISPLAY_CATEGORIES_ON_POSTINFO = True

CSS_FILE = 'custom.css'
STATIC_PATHS = ['theme/css', 'images']
