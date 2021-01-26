#!/usr/bin/env python
# coding=utf-8

import os

import logger as log
import err
import utils as u
import const as c


def obfuscate_code(data, enable=False, id=3):
    coalgo(data, enable, id)

def obfuscate_file(filename, enable=False, id=3):
    data = u.read_file(filename)
    coalgo(data, enable, id)
    
def coalgo(data, enable, id):
    if id == 3:
        coalgo3(data, enable)
    elif id == 2:
        coalgo2(data, enable)
    elif id == 1:
        coalgo1(data, enable)
    else:
        u.helper(err.FileNotFound)

def coalgo1(data, enable=False):
    if data == None:
        u.helper(err.NoDataInput, False)
    # TODO: implement coalgo1

def coalgo2(data, enable=False):
    if data == None:
        u.helper(err.NoDataInput, False)
    # TODO: implement coalgo2

def charmap():
    newer = [""] * c.NUMBER
    spec_list = ["_", "-"]
    for i in range(c.NUMBER):
        newer[i] = spec_list[1] + str(i/c.BITNUM) + spec_list[0] + str(i%c.BITNUM)
    return newer

def coalgo3(data, enable=False):
    filename = input('\033[32mSave result as a file? Please special a name: \033[0m')
    u.processing_bar('\033[33mEncoding...\033[0m')
    
    ret = ''
    mapset = charmap()
    for j in data:
        idx = ord(j)
        if idx >= 97 and idx <= 122:
            # FIXME: n cannot large than the size of mapset and wrong result output
            n = idx - 97
            ret += mapset[n]
            if enable == True:
                log.debug(ret)

    newstr = ''
    for k in range(len(data)):
        newstr += mapset[k]
        u.save_file(filename, newstr) 
    print('\033[31mAll done, good job!\033[0m')
