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

def is_file_exist(filename):
    f = open(filename, 'r')
    # TODO: find the error while read the data from the file
    # f.read()
