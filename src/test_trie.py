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


def test_check_input_false_many_bad_characters():
    """Test that a token we believe to be bad returns False."""
    from trie import Trie
    trie = Trie()
    token = '$!*&#^|'
    assert trie._check_token(token) is False


def test_check_input_false_words_space():
    """Test that a token we believe to be bad returns False."""
    from trie import Trie
    trie = Trie()
    token = 'my computer'
    assert trie._check_token(token) is False


def test_check_input_true_with_apostrophe():
    """Test that a token with an apostrophe returns True."""
    from trie import Trie
    trie = Trie()
    token = "computer's"
    assert trie._check_token(token)


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


def test_contains_given_string_one_string_():
    """Test that a given string is in the list."""
    from trie import Trie
    trie = Trie()
    token = 'pig'
    trie.insert(token)
    assert trie.contains(token)


def test_contains_trie_has_two():
    """Test insertion of second token on trie."""
    from trie import Trie
    trie = Trie()
    token = 'pig'
    token2 = 'piglet'
    trie.insert(token)
    trie.insert(token2)
    assert trie.contains(token)
    assert trie.contains(token2)


def test_contains_on_partial():
    """Test contains returns false on partial match."""
    from trie import Trie
    trie = Trie()
    token = 'piglet'
    trie.insert(token)
    assert trie.contains('pig') is False


def test_contains_on_shorter():
    """Test contains returns false on non-inserted longer word."""
    from trie import Trie
    trie = Trie()
    token = 'pig'
    trie.insert(token)
    assert trie.contains('piglet') is False
