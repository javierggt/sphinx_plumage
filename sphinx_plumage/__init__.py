from os import path

def setup(app):
    app.add_html_theme('plumage', path.abspath(path.dirname(__file__)))
