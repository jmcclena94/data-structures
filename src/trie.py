# coding=utf-8
class Trie(object):
    """Trie object."""

    def __init__(self):
        """Init Trie container."""
        self.container = {}

    def insert(self, token):
        """Insert token into the Trie."""
        end = '$'
        temp_container = self.container
        for letter in token:
            temp_container = temp_container.setdefault(letter, {})
        temp_container[end] = end

    def contains(self, token):
        """Given a string returns boolean if in or not in contianer."""
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

