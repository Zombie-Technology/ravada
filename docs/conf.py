extensions = [
    'sphinx-prompt'
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'RavadaVDI'
copyright = u'2018, RavadaVDI'
author = u'Ravada Team'

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = 'en'

# Theme options
html_theme_options = {
    # 'typekit_id': 'hiw1hhg',
    # 'analytics_id': '',
    # 'sticky_navigation': True  # Set to False to disable the sticky nav while scrolling.
    'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
    'collapse_navigation': False,  # Collapse navigation (False makes it tree-like)
    # 'display_version': True,  # Display the docs version
    # 'navigation_depth': 4,  # Depth of the headers shown in the navigation bar
}

html_logo = 'img/logo_ravada.png'
