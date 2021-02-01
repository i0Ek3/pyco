#!/usr/bin/env python
# coding=utf-8

import string

import err
import utils as u
import const as c


def obfuscate_code(data, enable=False):
    coalgo(data, enable)

def obfuscate_file(filename, enable=False):
    data = u.read_file(filename)
    coalgo(data, enable)
    
def charmap():
    newer = [""] * (c.NUMBER + 1)
    spec_list = ["_", "-"]
    for i in range(0, c.NUMBER-1):
        newer[i] = spec_list[1] + str(int(i/c.BITNUM)) + spec_list[0] + str(i%c.BITNUM)
    return newer

def coalgo(data, enable=False):
    if data == None:
        u.helper(err.NoDataInput, False)

    filename = input('\033[32mSave result as a file? Please special a name: \033[0m')
    u.processing_bar('\033[33mEncoding...\033[0m')
    
    ret = ''
    mapset = charmap()
    for j in data.lower():
        idx = ord(j)

        if idx >= 97 and idx <= 122:
            n = idx - 97
            ret += mapset[n]
            u.logu(enable, ret)
        f = open(filename, 'w')
        f.write(ret)
        f.close()
    
    print('\033[31mAll done, good job!\033[0m')
    return ret
