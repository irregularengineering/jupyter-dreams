"""
Jupyter Method
"""

import re
import inspect
from itertools import zip_longest
from enum import Enum
from typing import List, MethodWrapperType, Any, Tuple, Dict

from pewpyter.jupyter_forms.jupyter_argument import JupyterArgument


class JupyterMethod(object):
    """
    Method metadata to enable setting of argument values and building of invocation string
    """
    DESCRIPTION_REGEX = r'\n?(.*)(\n:)?'
    ARG_REGEX_FORMAT = r':param[^\S\n]+{}:[^\S\n]*(.*)\n*'
    IGNORE_FIRST_ARGS = ['self', 'cls']

    def __init__(self, method: MethodWrapperType):
        self.method = method
        self.name = method.__name__
        self.arguments = self._get_arguments(self.method)
        self.description = self._get_method_description(self.method)

    @staticmethod
    def _get_arguments(method: MethodWrapperType) -> List[JupyterArgument]:
        """
        Extract the argument names and types from the method definition (including argument hints)

        :param method: method reference
        :return:
        """
        arguments = list()
        arg_info = inspect.getfullargspec(method)
        arg_names = arg_info.args
        arg_default_map = JupyterMethod._get_arg_defaults_dict(arg_info.defaults, arg_names)
        if arg_names and arg_names[0] in JupyterMethod.IGNORE_FIRST_ARGS:
            del arg_names[0]
        for arg_name in arg_names:
            arg_type = arg_info.annotations.get(arg_name)
            arg_default = arg_default_map.get(arg_name)
            description = JupyterMethod._get_arg_description(method, arg_name)
            arguments.append(JupyterArgument(arg_name, arg_type, description, arg_default))
        return arguments

    @staticmethod
    def _get_arg_defaults_dict(arg_defaults: (Tuple[Any], None), arg_names: List[str]) -> Dict[str, Any]:
        """
        Retrieve dict of argument name to default value.

        Note that arg_info.defaults returns None if no defaults are defined, else a tuple of default values.

        :param arg_defaults: tuple of default values (output from inspect.getfullargspec().defaults)
        :param arg_names: list of argument names (output from inspect.getfullargspec().args)
        :return:
        """
        arg_defaults_list = list(arg_defaults) if arg_defaults else list()
        return {arg: default for arg, default in zip_longest(reversed(arg_names), reversed(arg_defaults_list))}

    @staticmethod
    def _get_arg_description(method: MethodWrapperType, arg: str) -> str:
        """
        Get description of argument from doc string.
        Takes text following ":param <param_name>:"

        :param method: method reference
        :param arg: argument name
        :return: description
        """
        if not method.__doc__:
            return ''
        arg_regex = JupyterMethod.ARG_REGEX_FORMAT.format(arg)
        return JupyterMethod._get_regex_match(arg_regex, method.__doc__)

    @staticmethod
    def _get_method_description(method: MethodWrapperType) -> str:
        """
        Extract method description from docstring.
        Takes everything preceding ":param" or ":return"

        :param method: method reference
        :return: description
        """
        if not method.__doc__:
            return ''
        return JupyterMethod._get_regex_match(JupyterMethod.DESCRIPTION_REGEX, method.__doc__)

    @staticmethod
    def _get_regex_match(regex: str, text: str) -> str:
        """
        Return first regex match as str.  If no matches, return empty string.

        :param regex:
        :param text:
        :return: first match
        """
        match = re.search(regex, text)
        if not match:
            return ''
        return match.groups()[0].strip()

    def build_call_string(self, obj_name: str = None) -> str:
        """
        Build method call string including arguments

        :param obj_name: optional name of object to which method belongs
        :return: method invocation
        """
        argument_list = list()
        for argument in self.arguments:
            method_input = repr(argument.value)
            if argument.type and issubclass(argument.type, Enum):
                method_input = str(argument.type(argument.value))
            argument_list.append(argument.name + '=' + method_input)
        prefix = obj_name + '.' if obj_name else ''
        return '{}{}({})'.format(prefix, self.name, ', '.join(argument_list))

    def __str__(self) -> str:
        return str(dict(
            method=self.method,
            name=self.name,
            description=self.description,
            arguments=[str(argument) for argument in self.arguments]
        ))
