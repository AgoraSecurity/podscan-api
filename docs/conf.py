import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Podscan API Client"
copyright = "2024, AgoraSecurity"
author = "AgoraSecurity"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
]

autodoc_member_order = "bysource"
