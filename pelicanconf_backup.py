#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dstath'
SITENAME = u'Εργαστήριο Χωρικής Ανάλυσης, Γεωγραφικών \n Πληροφοριακών Συστημάτων και Θεματικής Χαρτογραφίας <BR>'
SITESUBTITLE = u'Τμήμα Μηχανικών Χωροταξίας, Πολεοδομίας και Περιφερειακής Ανάπτυξης <BR> Πανεπιστήμιο Θεσσαλίας, Πολυτεχνική Σχολή'

SITEURL = 'https://geographer.gr/gislab'

PATH = 'content'

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = u'Greek'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (
    ('Προφίλ', '/index.html'),
    ('Προσωπικό', '/pages/prosopiko.html'),
    ('Συνεργασίες', '/pages/synergasies.html'),
    ('Υποδομή', '/pages/ypodomi.html'),
    ('Ανακοινώσεις', '/pages/news.html'),
    ('Επικοινωνία', '/pages/contact.html'),
)


THEME = "themes/pelican-blueidea"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [	'assets',]

THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

LOAD_CONTENT_CACHE = False

STATIC_PATHS = ['images']





# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = False

# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = False

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = False

# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = False

# Display the search form
DISPLAY_SEARCH_FORM = False

# Sort pages list by a given attribute
#PAGES_SORT_ATTRIBUTE = 'Title'


# Blogroll
#LINKS 

# Social widget
SOCIAL =[]
