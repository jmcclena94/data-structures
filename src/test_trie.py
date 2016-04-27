# coding=utf-8
def test_insert_one_token():
    """Test when token is inserted into the trie correctly."""
    from trie import Trie
    trie = Trie()
    token = 'pig'
    trie.insert(token)
    assert trie.container == {'p': {'i': {'g': {'$': '$'}}}}


def test_insert_second_token():
    """Test insertion of second token on trie."""
    from trie import Trie
    trie = Trie()
    token = 'pig'
    token2 = 'piglet'
    trie.insert(token)
    assert trie.container == {'p': {'i': {'g': {'$': '$'}}}}
    trie.insert(token2)
    assert trie.container == {'p': {'i': {'g':
                                          {'$': '$',
                                           'l': {'e': {'t': {'$': '$'}}}
                                           }
                                          }
                                    }
                              }


def test_contains_given_string_one_string():
    """Test that a given string is in the list."""
    from trie import Trie
    trie = Trie()
    token = 'pig'
    trie.insert(token)
    assert trie.contains(token)
