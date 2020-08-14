"""
JupyterForm - A UI builder for Jupyter
"""

from datetime import date, datetime
from enum import Enum
from collections import namedtuple
from typing import ClassVar, List

import ipywidgets
from IPython.display import display

from pewpyter.jupyter_forms.jupyter_method import JupyterMethod
from pewpyter.jupyter_forms.jupyter_argument import JupyterArgument
from pewpyter.jupyter_forms.jupyter_argument_types import BigStr
from pewpyter import utils

ArgumentTypeAssociation = namedtuple('ArgumentTypeWidgetType', ['base_class', 'widget_type'])
WidgetAssociation = namedtuple('WidgetArgumentAssociation', ['widget', 'argument'])


class JupyterForm(object):
    """
    JupyterForm - A UI builder for Jupyter
    """
    ARGUMENT_TYPE_ASSOCIATIONS = [
        ArgumentTypeAssociation(Enum, ipywidgets.Dropdown),
        ArgumentTypeAssociation(list, ipywidgets.Textarea),
        ArgumentTypeAssociation(dict, ipywidgets.Textarea),
        ArgumentTypeAssociation(datetime, ipywidgets.Datetime),
        ArgumentTypeAssociation(date, ipywidgets.DatePicker),
        ArgumentTypeAssociation(bool, ipywidgets.Checkbox),
        ArgumentTypeAssociation(int, ipywidgets.IntText),
        ArgumentTypeAssociation(float, ipywidgets.FloatText),
        ArgumentTypeAssociation(BigStr, ipywidgets.Textarea),
        ArgumentTypeAssociation(str, ipywidgets.Text)
    ]
    DEFAULT_WIDGET_TYPE = ipywidgets.Text
    ENUM_FORMAT = '{}.{}'

    def __init__(self, jupyter_method: JupyterMethod, obj_name: str = None):
        self._jupyter_method = jupyter_method
        self._widget_associations = self._build_widgets(self._jupyter_method)
        self._obj_name = obj_name

    @staticmethod
    def _build_widgets(jupyter_method: JupyterMethod) -> List[WidgetAssociation]:
        """
        Build widgets from method definition and return List of widget associations

        :param jupyter_method:
        :return:
        """
        widget_associations = list()
        for argument in jupyter_method.arguments:
            widget_type = JupyterForm._get_object_type(argument)
            widget = JupyterForm._get_widget(argument, widget_type)
            widget_associations.append(WidgetAssociation(widget, argument))
        return widget_associations

    @staticmethod
    def _get_object_type(argument: JupyterArgument) -> ClassVar:
        """
        Get widget type based on prioritized list of associations

        :param argument:
        :return:
        """
        for argument_type_association in JupyterForm.ARGUMENT_TYPE_ASSOCIATIONS:
            if issubclass(argument.type, argument_type_association.base_class):
                return argument_type_association.widget_type
        return JupyterForm.DEFAULT_WIDGET_TYPE

    @staticmethod
    def _get_widget(argument: JupyterArgument, widget_type: ClassVar) -> ipywidgets.Widget:
        """
        Create a widget for argument

        :param argument:
        :param widget_type:
        :return:f
        """
        widget = widget_type(description=argument.name)
        if issubclass(argument.type, Enum):
            widget.options = [item.value for item in argument.type]
            if argument.default.value is not None:
                widget.value = argument.default.value
        elif argument.default is not None:
            widget.value = argument.default
        return widget

    def display_ui(self):
        """
        Display user interface in Jupyter
        """
        elements = list()
        for widget_association in self._widget_associations:
            elements.append(ipywidgets.HBox([
                widget_association.widget,
                ipywidgets.Label(value=widget_association.argument.description)
            ]))

        execute_button = ipywidgets.Button(description='Generate Code')
        execute_button.on_click(self._on_button_click)
        display(
            ipywidgets.Label(value=self._jupyter_method.description),
            ipywidgets.VBox(elements),
            execute_button
        )

    def _get_call_string(self) -> str:
        """
        Generate method call string

        :return: method invocation
        """
        for widget_association in self._widget_associations:
            widget_association.argument.set_value(widget_association.widget.value)
        return self._jupyter_method.build_call_string(obj_name=self._obj_name)

    def _on_button_click(self, _button):
        """
        Handle execute button click
        """
        utils.create_code_cell(self._get_call_string())
