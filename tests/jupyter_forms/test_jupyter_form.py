# pylint: disable=missing-docstring,redefined-outer-name,protected-access
"""
Tests for Jupyter Form
"""

from datetime import date, datetime

import ipywidgets

from pewpyter.jupyter_forms.jupyter_argument_types import BigStr
from pewpyter.jupyter_forms import JupyterForm, JupyterMethod, JupyterArgument
from tests.jupyter_forms import fake_methods as fm


def test_get_object_type():
    assert JupyterForm._get_object_type(JupyterArgument('arg', str, 'desc', None)) == ipywidgets.Text
    assert JupyterForm._get_object_type(JupyterArgument('arg', BigStr, 'desc', None)) == ipywidgets.Textarea
    assert JupyterForm._get_object_type(JupyterArgument('arg', int, 'desc', None)) == ipywidgets.IntText
    assert JupyterForm._get_object_type(JupyterArgument('arg', float, 'desc', None)) == ipywidgets.FloatText
    assert JupyterForm._get_object_type(JupyterArgument('arg', date, 'desc', None)) == ipywidgets.DatePicker
    assert JupyterForm._get_object_type(JupyterArgument('arg', datetime, 'desc', None)) == ipywidgets.Datetime
    assert JupyterForm._get_object_type(JupyterArgument('arg', bool, 'desc', None)) == ipywidgets.Checkbox
    assert JupyterForm._get_object_type(JupyterArgument('arg', list, 'desc', None)) == ipywidgets.Textarea
    assert JupyterForm._get_object_type(JupyterArgument('arg', dict, 'desc', None)) == ipywidgets.Textarea
    assert JupyterForm._get_object_type(JupyterArgument('arg', fm.FakeEnum, 'desc', None)) == ipywidgets.Dropdown
    assert JupyterForm._get_object_type(JupyterArgument('arg', bytes, 'desc', None)) == ipywidgets.Text


def test_get_widget():
    widget = JupyterForm._get_widget(JupyterArgument('arg', BigStr, 'desc', 'default'), ipywidgets.Textarea)
    assert isinstance(widget, ipywidgets.Textarea)
    assert widget.description == 'arg'
    assert widget.value == 'default'


def test_get_widget_enum():
    widget = JupyterForm._get_widget(JupyterArgument('arg', fm.FakeEnum, 'desc', fm.FakeEnum.BOJACK),
                                     ipywidgets.Dropdown)
    assert isinstance(widget, ipywidgets.Dropdown)
    assert widget.options == (fm.FakeEnum.BOJACK.value, fm.FakeEnum.TODD.value, fm.FakeEnum.DIANE.value)
    assert widget.description == 'arg'
    assert widget.value == fm.FakeEnum.BOJACK.value


def test_get_call_str():
    jupyter_method = JupyterMethod(fm.fake_annotated)
    jupyter_form = JupyterForm(jupyter_method)
    jupyter_form._widget_associations[0].widget.value = 'yo'
    assert jupyter_form._get_call_string() == "fake_annotated(wut='yo')"


def test_get_call_str_multiple():
    jupyter_method = JupyterMethod(fm.fake_many_default)
    jupyter_form = JupyterForm(jupyter_method)
    jupyter_form._widget_associations[0].widget.value = 99
    jupyter_form._widget_associations[1].widget.value = False
    jupyter_form._widget_associations[2].widget.value = 'yo'
    jupyter_form._widget_associations[3].widget.value = datetime(2018, 8, 7)
    assert jupyter_form._get_call_string() == \
           "fake_many_default(xint=99, xbool=False, xstr='yo', xdate=datetime.datetime(2018, 8, 7, 0, 0))"


def test_get_call_str_class():
    jupyter_method = JupyterMethod(fm.FakeClass.fake_instance_method)
    jupyter_form = JupyterForm(jupyter_method)
    jupyter_form._widget_associations[0].widget.value = 'no'
    assert jupyter_form._get_call_string() == "fake_instance_method(yes='no')"
