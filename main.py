#!/usr/bin/env python
# coding=utf-8

import obfuscate
import deobfuscate

def main():
    hi = input("Which option you want to take? [ob or de]: ")

    if hi == 'ob':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            obfuscate_code()
        elif ctx == 'file':
            obfuscate_file()
        else:
            print("Wrong input.")
    elif hi == 'de':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            deobfuscate_code()
        elif ctx == 'file':
            deobfuscate_file()
        else:
            print("Wrong input.")
    else:
        print("Wrong input.")


#
#if __name__ == '__main()__':
    main()
