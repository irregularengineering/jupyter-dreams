# pylint: disable=unused-argument,invalid-name,dangerous-default-value,missing-docstring
"""
Fake methods for testing Giraffe
"""

from datetime import date
from enum import Enum


class FakeEnum(Enum):
    BOJACK = 'Bojack'
    TODD = 'Todd'
    DIANE = 'Diane'


class FakeClass(object):
    def fake_instance_method(self, yes: str):
        """
        Fake instance method

        :param yes: no
        :return:
        """
        pass

    def fake_instance_method_default(self, yes: str = 'yo'):
        """
        Fake instance method

        :param yes: no
        :return:
        """
        pass

    @classmethod
    def fake_class_method(cls, yo: int):
        """
        Fake class method

        :param yo: yoyo
        :return:
        """
        pass

    @classmethod
    def fake_class_method_default(cls, yo: int = -7):
        """
        Fake class method

        :param yo: yoyo
        :return:
        """
        pass

    @staticmethod
    def fake_static_method(huh: float):
        """
        Fake static method

        :param huh: why
        :return:
        """
        pass

    @staticmethod
    def fake_static_method_default(huh: float = 123456.789):
        """
        Fake static method

        :param huh: why
        :return:
        """
        pass

    def __repr__(self):
        return 'fake_class'


def fake_nodocstring():
    pass


def fake_weird_docstring():
    """Fake weird docstring"""
    pass


def fake_weird_arg(pony):
    """Fake weird arg
    :param pony: yep, pony"""
    pass


def fake_nothing():
    """
    Fake nothing

    :return:
    """
    pass


def fake_unannotated(wut):
    """
    Fake unannotated

    :param wut:
    :return:
    """
    pass


def fake_unannotated_default(wut=67):
    """
    Fake unannotated

    :param wut:
    :return:
    """
    pass


def fake_annotated(wut: str):
    """
    Fake annotated

    :param wut: hey now
    :return:
    """
    pass


def fake_annotated_default(wut: str = 'wutup'):
    """
    Fake annotated

    :param wut: hey now
    :return:
    """
    pass


def fake_dict(wut: dict):
    """
    Fake dict

    :param wut: something
    :return:
    """
    pass


def fake_dict_default(wut: dict = {3: 4, 'yo': 'wutup'}):
    """
    Fake dict

    :param wut: something
    :return:
    """
    pass


def fake_obj(hey: FakeClass):
    """
    Fake object

    :param hey: it's a class
    :return:
    """
    pass


def fake_enum(hollywoo: FakeEnum):
    """
    Fake enum

    :param hollywoo: horsin' around
    :return:
    """
    pass


def fake_enum_default(hollywoo: FakeEnum = FakeEnum.TODD):
    """
    Fake enum

    :param hollywoo: horsin' around
    :return:
    """
    pass


def fake_many(xint: int, xbool: bool, xstr: str, xdate: date):
    """
    These are some things you should fill out to make your life better

    :param xint: Enter an integer
    :param xbool: Enter a boolean
    :param xstr: Enter a string
    :param xdate: Enter a date
    :return:
    """
    pass


def fake_many_default(xint: int, xbool: bool = True, xstr: str = 'wut', xdate: date = date(2018, 6, 10)):
    """
    These are some things you should fill out to make your life better

    :param xint: Enter an integer
    :param xbool: Enter a boolean
    :param xstr: Enter a string
    :param xdate: Enter a date
    :return:
    """
    pass
