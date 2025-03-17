project = "BMDS User Guide"
copyright = "MIT License"

extensions = ["sphinx.ext.githubpages", "myst_nb", "sphinx_design", "sphinx_tippy"]
souce_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}
templates_path = ["_templates"]

exclude_patterns = []

numfig = True
numfig_format = {
    "code-block": "Listing %s.",
    "figure": "Figure %s.",
    "section": "Section",
    "table": "Table %s.",
}

myst_links_external_new_tab = True
myst_heading_anchors = 6
myst_enable_extensions = [
    "attrs_inline",
    "colon_fence",
    "dollarmath",
    "fieldlist",
    "html_image",
    "smartquotes",
]

# HTML settings
html_favicon = "_static/img/favicon.ico"
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["css/style.css"]
html_js_files = ["js/site.js"]
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "img/epa-seal.svg",
    "dark_logo": "img/epa-seal.svg",
    "source_repository": "https://github.com/USEPA/bmds-user-guide",
    "source_branch": "main",
    "source_directory": "docs/",
}

# Latex / PDF settings
latex_elements = {
    "printindex": "",
    "sphinxsetup": "hmargin={0.9in,0.9in}, vmargin={0.9in,0.9in}, marginpar=1.0in",
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "figure_align": "htbp",
}
