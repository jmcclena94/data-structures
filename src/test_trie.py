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


def test_traversal():
    """Test traversal on trie."""
    from trie import Trie
    word_list = []
    trie = Trie()
    token1 = 'power'
    token2 = 'free'
    trie.insert(token1)
    trie.insert(token2)
    for word in trie.traversal(start=trie.container):
        word_list.append(word)
    assert token1 in word_list
    assert token2 in word_list


def test_traversal_on_similar():
    """Test traversal on trie with similar words."""
    from trie import Trie
    word_list = []
    trie = Trie()
    token1 = 'free'
    token2 = 'freedom'
    trie.insert(token1)
    trie.insert(token2)
    for word in trie.traversal(start=trie.container):
        word_list.append(word)
    assert token1 in word_list
    assert token2 in word_list


def test_traversal_no_words():
    """Test traversal on trie with no words."""
    from trie import Trie
    word_list = []
    trie = Trie()
    for word in trie.traversal(start=trie.container):
        word_list.append(word)
    assert word_list == []


def test_traversal_with_apostrophe():
    """Test traversal on trie with apostrophe."""
    from trie import Trie
    word_list = []
    trie = Trie()
    token1 = "blade's"
    token2 = "fortune's"
    trie.insert(token1)
    trie.insert(token2)
    for word in trie.traversal(start=trie.container):
        word_list.append(word)
    assert token1 in word_list
    assert token2 in word_list


def test_autocomplete_two_words_from_root():
    """Test that autocomplete functions when input token is at the root."""
    from trie import Trie
    trie = Trie()
    token1 = "rifle"
    token2 = "adze"
    token3 = "rifleman"
    trie.insert(token1)
    trie.insert(token2)
    trie.insert(token3)
    auto = trie.autocomplete('rif')
    assert token1 in auto
    assert token3 in auto
    assert token2 not in auto


def test_autocomplete_not_from_root():
    """Test that autocomplete functions when input token is in trie not root."""
    from trie import Trie
    trie = Trie()
    rifle = "rifle"
    adze = "adze"
    rifleman = "rifleman"
    owl = "owl"
    owled = "owled"
    owl_s = "owl's"
    word_list = [rifle, adze, rifleman, owl, owled, owl_s]
    for indx in word_list:
        trie.insert(indx)
    auto = trie.autocomplete('owl')
    assert owl_s in auto
    assert owled in auto
    assert owl in auto
    assert adze not in auto


def test_autocomplete_on_non_existent_token():
    """Test that autocomplete returns empty list if token not in trie."""
    from trie import Trie
    trie = Trie()
    token1 = "rifle"
    token2 = "adze"
    token3 = "rifleman"
    trie.insert(token1)
    trie.insert(token2)
    trie.insert(token3)
    auto = trie.autocomplete('goat')
    assert auto == []


def test_autocomplete_greater_than_five_possibilities():
    """Test that autocomplete only returns a list of 4 when more available."""
    from trie import Trie
    trie = Trie()
    rain = 'rain'
    rain_s = "rain's"
    rainy = 'rainy'
    raining = 'raining'
    rainstorm = 'rainstorm'
    word_list = [rain, rain_s, rainy, raining, rainstorm]
    for indx in word_list:
        trie.insert(indx)
    assert len(trie.autocomplete(rain)) == 4
