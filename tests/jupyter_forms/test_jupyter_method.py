# pylint: disable=redefined-outer-name,missing-docstring,invalid-name
"""
Tests for Jupyter Method
"""

from datetime import date

import pytest

from pewpyter.jupyter_forms.jupyter_method import JupyterMethod
from tests.jupyter_forms import fake_methods as fm
from tests.jupyter_forms.fake_methods import FakeEnum


@pytest.fixture
def fake_class():
    return fm.FakeClass()


def test_fake_nodocstring():
    jupyter_method = JupyterMethod(fm.fake_nodocstring)
    assert jupyter_method.description == ''
    assert jupyter_method.arguments == list()
    assert jupyter_method.build_call_string() == 'fake_nodocstring()'


def test_fake_nothing():
    jupyter_method = JupyterMethod(fm.fake_nothing)
    assert jupyter_method.description == 'Fake nothing'
    assert jupyter_method.arguments == list()
    assert jupyter_method.build_call_string() == 'fake_nothing()'


def test_weird_doscstring():
    jupyter_method = JupyterMethod(fm.fake_weird_docstring)
    assert jupyter_method.description == 'Fake weird docstring'
    assert jupyter_method.arguments == list()
    assert jupyter_method.build_call_string() == 'fake_weird_docstring()'


def test_weird_arg():
    jupyter_method = JupyterMethod(fm.fake_weird_arg)
    assert jupyter_method.description == 'Fake weird arg'
    assert jupyter_method.arguments[0].name == 'pony'
    assert jupyter_method.arguments[0].type is None
    assert jupyter_method.arguments[0].description == 'yep, pony'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.build_call_string() == 'fake_weird_arg(pony=None)'
    jupyter_method.arguments[0].set_value('steve meathead')
    assert jupyter_method.build_call_string() == "fake_weird_arg(pony='steve meathead')"


def test_fake_unannotated():
    jupyter_method = JupyterMethod(fm.fake_unannotated)
    assert jupyter_method.arguments[0].name == 'wut'
    assert jupyter_method.arguments[0].type is None
    assert jupyter_method.arguments[0].description == ''
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.description == 'Fake unannotated'
    assert jupyter_method.build_call_string() == 'fake_unannotated(wut=None)'
    jupyter_method.arguments[0].set_value('banana')
    assert jupyter_method.build_call_string() == "fake_unannotated(wut='banana')"


def test_fake_unannotated_default():
    jupyter_method = JupyterMethod(fm.fake_unannotated_default)
    assert jupyter_method.arguments[0].name == 'wut'
    assert jupyter_method.arguments[0].type is None
    assert jupyter_method.arguments[0].description == ''
    assert jupyter_method.arguments[0].default == 67
    assert jupyter_method.description == 'Fake unannotated'
    assert jupyter_method.build_call_string() == 'fake_unannotated_default(wut=None)'
    jupyter_method.arguments[0].set_value('banana')
    assert jupyter_method.build_call_string() == "fake_unannotated_default(wut='banana')"


def test_fake_annotated():
    jupyter_method = JupyterMethod(fm.fake_annotated)
    assert jupyter_method.arguments[0].name == 'wut'
    assert jupyter_method.arguments[0].type == str
    assert jupyter_method.arguments[0].description == 'hey now'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.description == 'Fake annotated'
    assert jupyter_method.build_call_string() == 'fake_annotated(wut=None)'
    jupyter_method.arguments[0].set_value('banana')
    assert jupyter_method.build_call_string() == "fake_annotated(wut='banana')"


def test_fake_annotated_default():
    jupyter_method = JupyterMethod(fm.fake_annotated_default)
    assert jupyter_method.arguments[0].name == 'wut'
    assert jupyter_method.arguments[0].type == str
    assert jupyter_method.arguments[0].description == 'hey now'
    assert jupyter_method.arguments[0].default == 'wutup'
    assert jupyter_method.description == 'Fake annotated'
    assert jupyter_method.build_call_string() == 'fake_annotated_default(wut=None)'
    jupyter_method.arguments[0].set_value('banana')
    assert jupyter_method.build_call_string() == "fake_annotated_default(wut='banana')"


def test_fake_dict():
    jupyter_method = JupyterMethod(fm.fake_dict)
    assert jupyter_method.arguments[0].name == 'wut'
    assert jupyter_method.arguments[0].type == dict
    assert jupyter_method.arguments[0].description == 'something'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.description == 'Fake dict'
    jupyter_method.arguments[0].set_value({1: 2, 'x': 'y'})
    assert jupyter_method.build_call_string() == "fake_dict(wut={1: 2, 'x': 'y'})"


def test_fake_dict_default():
    jupyter_method = JupyterMethod(fm.fake_dict_default)
    assert jupyter_method.arguments[0].name == 'wut'
    assert jupyter_method.arguments[0].type == dict
    assert jupyter_method.arguments[0].description == 'something'
    assert jupyter_method.arguments[0].default == {3: 4, 'yo': 'wutup'}
    assert jupyter_method.description == 'Fake dict'
    jupyter_method.arguments[0].set_value({1: 2, 'x': 'y'})
    assert jupyter_method.build_call_string() == "fake_dict_default(wut={1: 2, 'x': 'y'})"


def test_fake_obj(fake_class):
    jupyter_method = JupyterMethod(fm.fake_obj)
    assert jupyter_method.arguments[0].name == 'hey'
    assert jupyter_method.arguments[0].type == fm.FakeClass
    assert jupyter_method.arguments[0].description == "it's a class"
    assert jupyter_method.description == 'Fake object'
    jupyter_method.arguments[0].set_value(fake_class)
    assert jupyter_method.build_call_string() == "fake_obj(hey=fake_class)"


def test_fake_enum():
    jupyter_method = JupyterMethod(fm.fake_enum)
    assert jupyter_method.arguments[0].name == 'hollywoo'
    assert jupyter_method.arguments[0].type == fm.FakeEnum
    assert jupyter_method.arguments[0].description == "horsin' around"
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.description == 'Fake enum'
    jupyter_method.arguments[0].set_value(fm.FakeEnum.BOJACK.value)
    assert jupyter_method.build_call_string() == "fake_enum(hollywoo=FakeEnum.BOJACK)"

def test_fake_enum_default():
    jupyter_method = JupyterMethod(fm.fake_enum_default)
    assert jupyter_method.arguments[0].name == 'hollywoo'
    assert jupyter_method.arguments[0].type == fm.FakeEnum
    assert jupyter_method.arguments[0].description == "horsin' around"
    assert jupyter_method.arguments[0].default == FakeEnum.TODD
    assert jupyter_method.description == 'Fake enum'
    jupyter_method.arguments[0].set_value(fm.FakeEnum.BOJACK.value)
    assert jupyter_method.build_call_string() == "fake_enum_default(hollywoo=FakeEnum.BOJACK)"


def test_fake_many():
    jupyter_method = JupyterMethod(fm.fake_many)
    assert jupyter_method.arguments[0].name == 'xint'
    assert jupyter_method.arguments[0].type == int
    assert jupyter_method.arguments[0].description == 'Enter an integer'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.arguments[1].name == 'xbool'
    assert jupyter_method.arguments[1].type == bool
    assert jupyter_method.arguments[1].description == 'Enter a boolean'
    assert jupyter_method.arguments[1].default is None
    assert jupyter_method.arguments[2].name == 'xstr'
    assert jupyter_method.arguments[2].type == str
    assert jupyter_method.arguments[2].description == 'Enter a string'
    assert jupyter_method.arguments[2].default is None
    assert jupyter_method.arguments[3].name == 'xdate'
    assert jupyter_method.arguments[3].type == date
    assert jupyter_method.arguments[3].description == 'Enter a date'
    assert jupyter_method.arguments[3].default is None
    assert jupyter_method.description == 'These are some things you should fill out to make your life better'
    jupyter_method.arguments[0].set_value(55)
    jupyter_method.arguments[1].set_value(True)
    jupyter_method.arguments[2].set_value('yo')
    jupyter_method.arguments[3].set_value(date(2018, 6, 8))
    assert jupyter_method.build_call_string() == \
           "fake_many(xint=55, xbool=True, xstr='yo', xdate=datetime.date(2018, 6, 8))"


def test_fake_many_default():
    jupyter_method = JupyterMethod(fm.fake_many_default)
    assert jupyter_method.arguments[0].name == 'xint'
    assert jupyter_method.arguments[0].type == int
    assert jupyter_method.arguments[0].description == 'Enter an integer'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.arguments[1].name == 'xbool'
    assert jupyter_method.arguments[1].type == bool
    assert jupyter_method.arguments[1].description == 'Enter a boolean'
    assert jupyter_method.arguments[1].default
    assert jupyter_method.arguments[2].name == 'xstr'
    assert jupyter_method.arguments[2].type == str
    assert jupyter_method.arguments[2].description == 'Enter a string'
    assert jupyter_method.arguments[2].default == 'wut'
    assert jupyter_method.arguments[3].name == 'xdate'
    assert jupyter_method.arguments[3].type == date
    assert jupyter_method.arguments[3].description == 'Enter a date'
    assert jupyter_method.arguments[3].default == date(2018, 6, 10)
    assert jupyter_method.description == 'These are some things you should fill out to make your life better'
    jupyter_method.arguments[0].set_value(55)
    jupyter_method.arguments[1].set_value(True)
    jupyter_method.arguments[2].set_value('yo')
    jupyter_method.arguments[3].set_value(date(2018, 6, 8))
    assert jupyter_method.build_call_string() == \
           "fake_many_default(xint=55, xbool=True, xstr='yo', xdate=datetime.date(2018, 6, 8))"


def test_fake_instance_method(fake_class):
    jupyter_method = JupyterMethod(fake_class.fake_instance_method)
    assert jupyter_method.arguments[0].name == 'yes'
    assert jupyter_method.arguments[0].type == str
    assert jupyter_method.arguments[0].description == 'no'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.description == 'Fake instance method'
    jupyter_method.arguments[0].set_value('Mr. Peanutbutter')
    assert jupyter_method.build_call_string() == "fake_instance_method(yes='Mr. Peanutbutter')"


def test_fake_instance_method_default(fake_class):
    jupyter_method = JupyterMethod(fake_class.fake_instance_method_default)
    assert jupyter_method.arguments[0].name == 'yes'
    assert jupyter_method.arguments[0].type == str
    assert jupyter_method.arguments[0].description == 'no'
    assert jupyter_method.arguments[0].default == 'yo'
    assert jupyter_method.description == 'Fake instance method'
    jupyter_method.arguments[0].set_value('Mr. Peanutbutter')
    assert jupyter_method.build_call_string() == "fake_instance_method_default(yes='Mr. Peanutbutter')"


def test_fake_class_method(fake_class):
    jupyter_method = JupyterMethod(fake_class.fake_class_method)
    assert jupyter_method.arguments[0].name == 'yo'
    assert jupyter_method.arguments[0].type == int
    assert jupyter_method.arguments[0].description == 'yoyo'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.description == 'Fake class method'
    jupyter_method.arguments[0].set_value(42)
    assert jupyter_method.build_call_string() == "fake_class_method(yo=42)"


def test_fake_class_method_default(fake_class):
    jupyter_method = JupyterMethod(fake_class.fake_class_method_default)
    assert jupyter_method.arguments[0].name == 'yo'
    assert jupyter_method.arguments[0].type == int
    assert jupyter_method.arguments[0].description == 'yoyo'
    assert jupyter_method.arguments[0].default == -7
    assert jupyter_method.description == 'Fake class method'
    jupyter_method.arguments[0].set_value(42)
    assert jupyter_method.build_call_string() == "fake_class_method_default(yo=42)"


def test_fake_static_method(fake_class):
    jupyter_method = JupyterMethod(fake_class.fake_static_method)
    assert jupyter_method.arguments[0].name == 'huh'
    assert jupyter_method.arguments[0].type == float
    assert jupyter_method.arguments[0].description == 'why'
    assert jupyter_method.arguments[0].default is None
    assert jupyter_method.description == 'Fake static method'
    jupyter_method.arguments[0].set_value(3.14)
    assert jupyter_method.build_call_string() == "fake_static_method(huh=3.14)"


def test_fake_static_method_default(fake_class):
    jupyter_method = JupyterMethod(fake_class.fake_static_method_default)
    assert jupyter_method.arguments[0].name == 'huh'
    assert jupyter_method.arguments[0].type == float
    assert jupyter_method.arguments[0].description == 'why'
    assert jupyter_method.arguments[0].default == 123456.789
    assert jupyter_method.description == 'Fake static method'
    jupyter_method.arguments[0].set_value(3.14)
    assert jupyter_method.build_call_string() == "fake_static_method_default(huh=3.14)"
