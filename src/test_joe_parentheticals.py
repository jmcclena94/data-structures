# coding=utf-8
import pytest


PAR_TABLE = [
    ('()', 0),
    ('()()', 0),
    (')))(((', -1),
    ('(asdfsa()sgdsa(asdfsa))(', 1),
    ('(as(dfsa()sgdsa(asdfsa)))', 0),
    ('(&%(^*$*#()!!!(932!$*@)))', 0),
    ('(', 1),
    (')', -1),
]


@pytest.mark.parametrize('string, result', PAR_TABLE)
def test_parenth(string, result):
    from joe_parentheticals import parenthetical
    assert parenthetical(string) == result
