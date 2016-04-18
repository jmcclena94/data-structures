# -*- coding: utf-8 -*-


class HashTable(object):
    """Hash Table Class."""

    def __init__(self, value):
        """Initialize hashtable of size value."""
        self.table = []
        for i in range(value):
            self.table.append([])

    def _hash(self, key):
        """Take a key and hash it. Return and integer."""
        hash_value = 0
        for character in key:
            hash_value += ord(character)
        return hash_value % len(self.table)

    def set(self, key, value):
        """Set the value using the key in the hash table."""
        self.table[self._hash(key)].append((key, value))

    def get(self, key):
        """Return value of a given key."""
        key_list = self.table[self._hash(key)]
        for vals in key_list:
            if vals[0] == key:
                return vals[1]

