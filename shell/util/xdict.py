#coding=utf8


# import string
# from datetime import datetime, timedelta
# import os
# import sys
# import logging

def merge(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
