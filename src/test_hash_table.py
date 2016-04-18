# -*- coding: utf-8 -*-


def test_hash():
    """Test hash function."""
    from hash_table import HashTable
    new_hash = HashTable(100)
    hashed = new_hash._hash('string')
    assert hashed < len(new_hash.table)
    assert isinstance(hashed, int)


def test_set():
    """Test set function."""
    from hash_table import HashTable
    new_hash = HashTable(1)
    new_hash.set('chicken', 'robot')
    assert new_hash.table[0][0][0] == 'chicken'
    assert new_hash.table[0][0][1] == 'robot'
    assert new_hash.table[0][0] == ('chicken', 'robot')
