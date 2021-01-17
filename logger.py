#!/usr/bin/env python
# coding=utf-8

import os

import err


def debug(ret, enable=False):
    print("----> %s\n" % ret)

def show_msg(type):
    if type == err.InputError:
        print('Input error.')
    elif type == err.UnknownError:
        print('Unknown error.')
    elif type == err.UnknownMode:
        print('Unknown mode.')
    elif type == err.NoDataInput:
        print('No data input.')
    elif type == err.NoDataRead:
        print('No data read.')
    elif type == err.FileNotFound:
        print('File not found.')

def is_none(str):
    if str:
        return False
    else:
        return True

def file_check(filename):
    return os.path.exists(filename)
