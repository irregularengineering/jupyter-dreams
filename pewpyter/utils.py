"""
Utils
"""

import base64
from enum import Enum

from IPython.display import Javascript, display
from IPython.utils.py3compat import str_to_bytes, bytes_to_str


class CellLocation(Enum):
    """
    Jupyter notebook cell location enum
    """
    ABOVE = 'above'
    BELOW = 'below'
    AT_BOTTOM = 'at_bottom'


def create_code_cell(code: str = '', where: CellLocation = 'below'):
    """
    Create a code cell in the IPython Notebook

    :param code: code to fill the new code cell with.
    :param where: where to add the new code cell
    """
    encoded_code = bytes_to_str(base64.b64encode(str_to_bytes(code)))
    display(Javascript('''
        var code = IPython.notebook.insert_cell_{0}('code');
        code.set_text(atob("{1}"));
    '''.format(where, encoded_code)))
