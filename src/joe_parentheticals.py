# coding=utf-8
import sys
import re


def parenthetical(parens):
    """Determine if a string has open, balanced, or broken parenthesis"""
    clean_str = re.sub(r'[^(+)]', '', parens)
    while clean_str is not '':
        if clean_str[0] == ')':
            return -1
        if clean_str[-1] == '(':
            return 1
        clean_str = clean_str.replace('()', '')
    return 0


if __name__ == '__main__':
    to_parse = sys.argv[1]
    parenthetical(to_parse)
