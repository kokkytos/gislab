#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'dstath'
SITENAME = u'Εργαστήριο Χωρικής Ανάλυσης, Γεωγραφικών \n Πληροφοριακών Συστημάτων και Θεματικής Χαρτογραφίας <BR>'
SITESUBTITLE = u'Τμήμα Μηχανικών Χωροταξίας, Πολεοδομίας και Περιφερειακής Ανάπτυξης <BR> Πανεπιστήμιο Θεσσαλίας, Πολυτεχνική Σχολή'

SITEURL = 'http://www.gislab.gr'
#SITEURL = ''

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
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MENUITEMS = (
    ('Προφίλ', '/'),
    ('Προσωπικό', '/pages/prosopiko'),
    ('Συνεργασίες', '/pages/synergasies'),
    ('Υποδομή', '/pages/ypodomi'),
    ('Δραστηριότητες', '/category/drastiriotites.html'),
	#('Έρευνα', '/pages/ereyna'),
    #('Δημοσιεύσεις', '/pages/dimosieyseis'),
	#('Δεδομένα', '/pages/data'),
    ('Επικοινωνία', '/pages/contact'),
)


THEME = "themes/pelican-blueidea"
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets','i18n_subsites']
#PLUGINS = ['assets']
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'


LOAD_CONTENT_CACHE = False

STATIC_PATHS = ['images','extra','extra/CNAME',]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/index.html': {'path': 'osm_map/index.html'},
    'extra/index_en.html': {'path': 'osm_map/index_en.html'},
}
READERS = {'html': None}

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'


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


######################## Friendly name for languages ################
# https://bernhard.scheirle.de/posts/2016/August/17/pelican-improved-display-of-translations/
language_lookup = {
    'en': u'English',
    'greek': u'Greek',
}

def lookup_lang_name(lang_code):
    return language_lookup[lang_code]

JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name,
}



# Multilingual settings


I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Spatial Analysis, GIS and Thematic Mapping Laboratory<BR>',
	'SITESUBTITLE' : 'Department of Planning and Regional Development <BR >University of Thessaly, School of Engineering',
        #'LOCALE': 'en_US',            #This is somewhat redundant with DATE_FORMATS, but IMHO more convenient
	'SOCIAL':'',
        'RELATIVE_URLS' : 'False',
	'MENUITEMS': [
            ('Profile','/en'),
	    ('Staff','/en/pages/prosopiko'),
	    ('Collaborations','/en/pages/synergasies'),
	    ('Infrastructure','/en/pages/ypodomi'),
	    ('Contact','/en/pages/contact'),
        ],
       'DELETE_OUTPUT_DIRECTORY' : 'True',
       'CACHE_PATH':'cache_en'      }
    }

#OUTPUT_SOURCES = True

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'el': '%a, %d %b %Y',
}

LOCALE = (
    'en_US', 'el_GR'     # On Unix/Linux
    )


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}


SHOW_TRANSLATIONS_LABEL = False #variable by Leonidas


GOOGLE_ANALYTICS = "UA-142147823-1"


SUMMARY_MAX_LENGTH = 50

