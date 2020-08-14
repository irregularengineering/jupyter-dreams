# pylint: disable=missing-docstring,invalid-name,redefined-outer-name
"""
Tests for Secrets
"""

import pytest

from pewpyter import Secrets
from pewpyter.secrets import SecretDoesNotExceptException, SecretsFileDoesNotExist


@pytest.fixture
def secrets():
    return Secrets(secrets_file='tests/resources/test_secrets')


def test_get_secret_success(secrets):
    assert secrets.get_secret('TestSection', 'username') == 'bojack'


def test_get_secret_file_does_not_exist():
    with pytest.raises(SecretsFileDoesNotExist):
        Secrets(secrets_file='tests/resources/not_test_secrets')


def test_get_secret_section_does_not_exist(secrets):
    with pytest.raises(SecretDoesNotExceptException):
        secrets.get_secret('NotTestSection', 'username')


def test_get_secret_param_does_not_exist(secrets):
    with pytest.raises(SecretDoesNotExceptException):
        secrets.get_secret('TestSection', 'api_key')
