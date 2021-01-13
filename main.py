#!/usr/bin/env python
# coding=utf-8

import obfuscate as ob
import deobfuscate as de

def main():
    hi = input("Which option you want to take? [ob or de]: ")

    if hi == 'ob':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            ob.obfuscate_code()
        elif ctx == 'file':
            ob.obfuscate_file()
        else:
            print("Wrong input.")
    elif hi == 'de':
        ctx = input("Which option you want to take? [code or file]: ")
        if ctx == 'code':
            de.deobfuscate_code()
        elif ctx == 'file':
            de.deobfuscate_file()
        else:
            print("Wrong input.")
    else:
        print("Wrong input.")


if __name__ == '__main()__':
    main()
