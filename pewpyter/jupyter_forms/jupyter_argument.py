"""
Jupyter Argument
"""

from typing import Any


class JupyterArgument(object):
    """
    Argument for JupyterMethod
    """
    def __init__(self, name: str, arg_type: type, description: str, default: Any):
        self.name = name
        self.type = arg_type
        self.description = description
        self.default = default
        self.value = None

    def set_value(self, value: Any):
        """
        Set the value for the argument

        :param value: anything you like
        """
        self.value = value

    def __str__(self) -> str:
        return str(self.__dict__)
