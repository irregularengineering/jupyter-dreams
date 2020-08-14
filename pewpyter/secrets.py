"""
Secrets Manager

Read secrets from ~/.secrets file
"""

import os
from configparser import ConfigParser


class SecretsFileDoesNotExist(Exception):
    """
    Thrown when secrets file does not exist
    """
    def __init__(self, secrets_file):
        message = 'Secrets file does not exist at {}'.format(secrets_file)
        super(SecretsFileDoesNotExist, self).__init__(message)


class SecretDoesNotExceptException(Exception):
    """
    Thrown when secret does not exist in local secrets file
    """
    def __init__(self, section, param, secrets_file):
        message = 'Secret "{}" does not exist under section "{}" in {}'.format(param, section, secrets_file)
        super(SecretDoesNotExceptException, self).__init__(message)


class Secrets(object):
    """
    Secrets Manager
    """
    SECRETS_FILE = '~/.secrets'

    def __init__(self, secrets_file: str = SECRETS_FILE):
        self._secrets_file = os.path.expanduser(secrets_file)
        if not os.path.exists(self._secrets_file):
            raise SecretsFileDoesNotExist(self._secrets_file)
        config = ConfigParser()
        config.read(self._secrets_file)
        self._secrets = {section: dict(config.items(section)) for section in config.sections()}

    def get_secret(self, section: str, param: str) -> str:
        """
        Fetch secret from local secrets file

        :param section: as str
        :param param: as str
        :return: secret value as str
        """
        if section not in self._secrets:
            raise SecretDoesNotExceptException(section, param, self._secrets_file)
        if param not in self._secrets[section]:
            raise SecretDoesNotExceptException(section, param, self._secrets_file)
        return self._secrets[section][param]
