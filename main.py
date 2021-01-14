#!/usr/bin/env python
# coding=utf-8

import obfuscate as ob
import deobfuscate as de
import logger as log


def main():
    hi = input("Which option you want to take? [ob or de]: ")

    if hi == 'ob':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            data = input('Please input the raw data: ')
            if log.is_none(data):
                log.show_msg(NoDataInput) 
            else:
                ob.obfuscate_code(data, True, 2)
        elif ctx == 'file':
            filename = input('Please input the filename: ')
            if log.is_none(filename):
                log.show_msg(NoDataInput)
            else:
                ob.obfuscate_file(filename, True)
        else:
            print("Wrong input.")
    elif hi == 'de':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            data = input('Please input the encode data: ')
            if log.is_none(data):
                log.show_msg(NoDataInput) 
            else:
                de.deobfuscate_code(data, True)
        elif ctx == 'file':
            filename = input('Please input the filename: ')
            if log.is_none(filename):
                log.show_msg(NoDataInput)
            else:
                de.deobfuscate_file(filename, True)
        else:
            print("Wrong input.")
    else:
        print("Wrong input.")


main()
