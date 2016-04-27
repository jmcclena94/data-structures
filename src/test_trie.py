# coding=utf-8
def test_check_input_true():
    """Test that a token we believe to be good returns True."""
    from trie import Trie
    trie = Trie()
    token = 'computer'
    assert trie._check_token(token)


def test_check_input_false():
    """Test that a token we believe to be bad returns False."""
    from trie import Trie
    trie = Trie()
    token = '$computer'
    assert trie._check_token(token) is False


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
