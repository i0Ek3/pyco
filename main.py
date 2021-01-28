#!/usr/bin/env python
# coding=utf-8

import sys
import string

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
            u.blank_check(data)
            if u.is_none(data):
                u.helper(err.NoDataInput) 
            else:
                newdata = data.replace(" ", "")
                tof = input('\033[32mWould you like enable debug mode? [True or False]: \033[0m')
                enable = u.true_or_false(tof) == True
                ob.obfuscate_code(newdata, enable, 3)
        elif ctx == 'file':
            filename = input('\033[32mPlease input the filename: \033[0m')
            if u.file_check(filename):
                tof = input('\033[32mWould you like enable debug mode? [True or False]: \033[0m')
                enable = u.true_or_false(tof)
                ob.obfuscate_file(filename, enable)
            else:
                u.helper(err.FileNotFound, False)
        else:
            print("\033[31mWrong input!\033[0m")
    elif hi == 'de':
        ctx = input("\033[34mWhich option you want to take? [code or file]: \033[0m")
        if ctx == 'code':
            data = input('\033[32mPlease input the encode data: \033[0m')
            if u.is_none(data):
                u.helper(err.NoDataInput) 
            else:
                newdata = data.replace(" ", "")
                tof = input('\033[32mWould you like enable debug mode? [True or False]: \033[0m')
                enable = u.true_or_false(tof) == True
                de.deobfuscate_code(newdata, enable)
        elif ctx == 'file':
            filename = input('\033[32mPlease input the filename: \033[0m')
            if not u.is_python_file(filename):
                answer = input('\033[31mWarning: %s is not Python file!\nWould you like to continue? [yes or no]\033[0m' % filename)
                if answer == 'yes':
            	    u.helper(err.YourOwnRisk, False)
                else:
            	    u.helper(err.SelfKilling)

            if u.file_check(filename):
                tof = input('\033[32mWould you like enable debug mode? [True or False]: \033[0m')
                enable = u.true_or_false(tof)
                save = input('\033[32mSave the result into file? [yes or no]: \033[0m')
                if save == "yes": 
                    de.deobfuscate_file(filename, enable, save)
                else:
                    de.deobfuscate_file(filename, enable)
            else:
                u.helper(err.FileNotFound, False)
        else:
            print("\033[31mWrong input!\033[0m")
    else:
        print("\033[31mWrong input!\033[0m")


main()
