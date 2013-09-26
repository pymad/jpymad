"""
Resource provider for plain filesystem resources.
"""

__all__ = ['FileResource']

import os
from contextlib import contextmanager

from .base import ResourceProvider

class FileResource(ResourceProvider):
    """
    File system resource provider.

    Uses the builtins open() to open ordinary files and os.listdir() to list
    directory contents.

    """
    def __init__(self, path):
        """
        Initialize the filesystem resource provider.

        :param string path: name of a filesystem object (file/folder).

        """
        self.path = path

    def open(self, name=''):
        return open(self._get_path(name))

    def listdir(self, name=''):
        return os.listdir(self._get_path(name))

    def get(self, name=''):
        return self.__class__(self._get_path(name))

    @contextmanager
    def filename(self, name=''):
        yield self._get_path(name)

    def _get_path(self, name):
        if not name:
            return self.path
        elif isinstance(name, list):
            return os.path.join(self.path, *name)
        else:
            return os.path.join(self.path, name)

    def provider(self):
        return self.__class__(os.path.dirname(self.path))

