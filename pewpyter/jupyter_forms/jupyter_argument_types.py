"""
Jupyter Argument Types
"""


class BigStr(str):
    """
    Subclass of string
    """
    def __init__(self, value='', encoding=None, errors='strict'):
        super(BigStr, self).__init__(value, encoding=encoding, errors=errors)
