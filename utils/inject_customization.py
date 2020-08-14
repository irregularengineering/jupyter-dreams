"""
Inject custom CSS or JS to make this actually useful
"""

import os
import shutil

from custom_js import CUSTOM_SNIPPIT_MENU_CODE

# CUSTOM_CSS_FILEPATH = "/home/root/.jupyter/custom/custom.css"
# CUSTOM_JS_FILEPATH = "/home/root/.jupyter/custom/custom.js"
CUSTOM_JS_FILEPATH = "/usr/local/lib/python3.6/site-packages/notebook/static/custom/custom.js"
CUSTOM_CSS_FILEPATH = "/usr/local/lib/python3.6/site-packages/notebook/static/custom/custom.css"
ADDTL_STYLESHEET = "styles.css"


def main():
    """Add some JS and CSS specified locations"""
    write_to_custom_js(CUSTOM_SNIPPIT_MENU_CODE)
    write_to_css(ADDTL_STYLESHEET, CUSTOM_CSS_FILEPATH)


def write_to_custom_js(string_to_append):
    """
    Append some JS to custom.js

    """
    with open(CUSTOM_JS_FILEPATH, 'w+') as fptr:
        fptr.write(string_to_append)


def write_to_css(stylesheet, css_path):
    """
    Append some CSS in Jupyter's preferred spot.
    Do it after 
    """
    content = ''
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open('{}/content/styles/{}'.format(current_dir, stylesheet), 'r') as styles:
        content += styles.read() + '\n'

    with open(css_path, 'w+') as fptr:
        fptr.write(content)


if __name__ == '__main__':
    main()
