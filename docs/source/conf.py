# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Renale'
copyright = '2024, Acemany'
author = 'Acemany'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['static']

# -- Options for HTML output
html_context = {
    "default_mode": "dark",
    "navbar_end": ["navbar-icon-links"]
}

html_css_files = ["styles.css"]

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
