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
    elif type == FileNotFoundError:
        print('File not found.')

def is_none(str):
    if str:
        return False

def file_check(filename):
    try:
        f = open(filename, 'r')
        data = f.read()
    except IOError as e:
        print(e)
