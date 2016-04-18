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


def test_get():
    """Test get fucntion."""
    from hash_table import HashTable
    new_hash = HashTable(100)
    new_hash.set('pirate', 'ninja')
    assert new_hash.get('pirate') == 'ninja'


def test_hash_on_word_list():
    """Test that hash works on a giant list of words."""
    from hash_table import HashTable
    import io
    new_hash = HashTable(500)
    file = io.open('/usr/share/dict/words')
    for i in range(250000):
        key = value = file.readline()
        new_hash.set(key, value)
        assert new_hash.get(key) == value
