import os
import sys

# Путь относительно файла conf.py
sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------

project = 'Практическая 3'
copyright = '2025, Юровский Никита'
author = 'Юровский Никита'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      # автодокументация из docstrings
    'sphinx.ext.napoleon',     # поддержка Google/NumPy стилей
    'sphinx.ext.viewcode',     # просмотр исходного кода
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Настройка для Napoleon (Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Настройки для autodoc
autodoc_member_order = 'groupwise'
autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']