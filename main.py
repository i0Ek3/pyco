#!/usr/bin/env python
# coding=utf-8

import sys
import string
import re

import obfuscate as ob
import deobfuscate as de
import logger as log
import err
import utils as u


def main():
    hi = input("Which option you want to take? [ob or de]: ")

    if hi == 'ob':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            data = input('Please input the raw data: ')
            if log.is_none(data):
                log.show_msg(err.NoDataInput) 
                sys.exit()
            else:
                # TODO: blank checking
                # for x in data:
                #    u.blank_check(x)
                ob.obfuscate_code(data, True, 2)
        elif ctx == 'file':
            filename = input('Please input the filename: ')
            if log.file_check(filename):
                ob.obfuscate_file(filename)
            else:
                log.show_msg(err.FileNotFound)
        else:
            print("Wrong input.")
    elif hi == 'de':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            data = input('Please input the encode data: ')
            if log.is_none(data):
                log.show_msg(err.NoDataInput) 
                sys.exit()
            elif data == ' ':
                log.show_msg(err.DoNotInputBlank)
            else:
                de.deobfuscate_code(data)
        elif ctx == 'file':
            filename = input('Please input the filename: ')
            if log.file_check(filename):
                de.deobfuscate_file(filename, True)
            else:
                log.show_msg(err.FileNotFound)
        else:
            print("Wrong input.")
    else:
        print("Wrong input.")


main()
