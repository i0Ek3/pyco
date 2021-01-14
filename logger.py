#!/usr/bin/env python
# coding=utf-8

InputError = 'input_error'
UnknownError = 'internal_error'
NoDataInput = 'no_data_input'

def debug(ret, enable=False):
    print("----> %s\n" % ret)

def show_msg(type):
    if type == InputError:
        print('Input error.')
    elif type == UnknownError:
        print('Internal error.')
    elif type == NoDataInput:
        print('No data input.')
    elif type == RuntimeError:
        print('Runtime error.')

def is_none(str):
    if str is None:
        return True
