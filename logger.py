#!/usr/bin/env python
# coding=utf-8

import os

import err


def debug(ret, enable=False):
    print("\033[32m----> %s\033[0m\n" % ret)

def show_msg(type):
    if type == err.InputError:
        print('\033[33mInput error!\033[0m')
    elif type == err.UnknownError:
        print('\033[33mUnknonwn error!\033[0m')
    elif type == err.UnknownMode:
        print('\033[33mUnknown mode!\033[0m')
    elif type == err.NoDataInput:
        print('\033[33mNo data input!\033[0m')
    elif type == err.NoDataRead:
        print('\033[33mNo data read!\033[0m')
    elif type == err.FileNotFound:
        print('\033[33mFile not found!\033[0m')
    elif type == err.MyOwnRisk:
        print('\033[33mMy own risk!\033[0m')

def is_none(str):
    if str:
        return False
    else:
        return True

def file_check(filename):
    return os.path.exists(filename)
