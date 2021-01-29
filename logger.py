#!/usr/bin/env python
# coding=utf-8

import err


def debug(ret):
    for i in range(len(ret)):
        result = "\033[32m\nret ----> {}.\033[0m\n"
        print(result.format(ret[i]))

def show_msg(type):
    if type == err.InputError:
        print('\033[34mInput error!\033[0m')
    elif type == err.UnknownError:
        print('\033[34mUnknonwn error!\033[0m')
    elif type == err.UnknownMode:
        print('\033[34mUnknown mode!\033[0m')
    elif type == err.NoDataInput:
        print('\033[34mNo data input!\033[0m')
    elif type == err.NoDataRead:
        print('\033[34mNo data read!\033[0m')
    elif type == err.FileNotFound:
        print('\033[34mFile not found!\033[0m')
    elif type == err.FileIsEmpty:
        print('\033[34mFile is empty!\033[0m')
    elif type == err.YourOwnRisk:
        print('\033[34mYour own risk!\033[0m')
    elif type == err.DoNotInputBlank:
        print('\033[34mDo not input blank!\033[0m')
    elif type == err.SelfKilling:
        print('\033[34mSelf killing!\033[0m')

def line(n, c):
    s = ""
    for i in range(n):
        s += c
    print(s)
