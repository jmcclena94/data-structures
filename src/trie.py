# coding=utf-8
import re


class Trie(object):
    """Trie object."""

    def __init__(self):
        """Init Trie container."""
        self.container = {}

    def _check_token(self, token):
        """Check if token input is valid input."""
        token = token.lower()
        check = re.sub(r'((^|\')([a-z]+))+$', '', token)
        if check == '':
            return True
        return False

    def insert(self, token):
        """Insert token into the Trie."""
        if self._check_token(token):
            end = '$'
            temp_container = self.container
            for letter in token:
                temp_container = temp_container.setdefault(letter, {})
            temp_container[end] = end
        else:
            return 'Not valid input.'

    def contains(self, token):
        """Given a string returns boolean if in or not in container."""
        temp_container = self.container
        for letter in token:
            try:
                temp_container = temp_container[letter]
            except KeyError:
                return False
        try:
            temp_container['$']
            return True
        except KeyError:
            return False

