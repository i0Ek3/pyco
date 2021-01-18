#!/usr/bin/env python
# coding=utf-8

import sys
#import string
#import re

import obfuscate as ob
import deobfuscate as de
import logger as log
import err
import utils as u


def main():
    hi = input("\033[34mWhich option you want to take? [ob or de]: \033[0m")

    if hi == 'ob':
        ctx = input("\033[34mWhich option you want to take? [code or file]: \033[0m")
        if ctx == 'code':
            data = input('\033[32mPlease input the raw data: \033[0m')
            if log.is_none(data):
                u.helper(err.NoDataInput) 
            else:
                # TODO: blank checking
                # for x in data:
                #    u.blank_check(x)
                ob.obfuscate_code(data, True, 2)
        elif ctx == 'file':
            filename = input('\033[32mPlease input the filename: \033[0m')
            if log.file_check(filename):
                ob.obfuscate_file(filename)
            else:
                u.helper(err.FileNotFound, False)
        else:
            print("\033[31mWrong input!\033[0m")
    elif hi == 'de':
        ctx = input("\033[34mWhich option you want to take? [code or file]: \033[0m")
        if ctx == 'code':
            data = input('\033[32mPlease input the encode data: \033[0m')
            if log.is_none(data):
                u.helper(err.NoDataInput) 
            elif data == ' ':
                u.helper(err.DoNotInputBlank, False)
            else:
                de.deobfuscate_code(data)
        elif ctx == 'file':
            filename = input('\033[32mPlease input the filename: \033[0m')
            if log.file_check(filename):
                de.deobfuscate_file(filename, True)
            else:
                u.helper(err.FileNotFound, False)
        else:
            print("\033[31mWrong input!\033[0m")
    else:
        print("\033[31mWrong input!\033[0m")


main()
