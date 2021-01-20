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
    for i in range(data):
        if enable == True:
            # TODO: transfer i
            log.debug(i, enable)
            if i == None:
                u.helper(err.InputError, False)
        else:
            # TODO: transfer i
            pass

def coalgo2(data, enable=False):
    # TODO: a --> -0_0, h --> -0_7, i --> -1_0, p --> -1_7
    if data == None:
        u.helper(err.NoDataInput, False)

def charmap(data):
    newer = [""] * c.NUMBER
    spec_list = ["_", "-"]
    for i in range(c.NUMBER):
        newer[i] = spec_list[1] + str(i/8) + spec_list[0] + str(i%8)
    return newer

# FIXME: wrong result here and cannot output the debug information
def coalgo3(data, enable=False):
    filename = input('\033[32mSave result as a file? Please special a name: \033[0m')
    u.processing_bar('\033[33mEncoding...\033[0m')
    
    newdata = charmap(data)
    for i in data:
        if i >= '97' and i <= '122':
            n = i - 97
            ret = newdata[n]
            if enable == True:
                log.debug(ret)

    newstr = ''
    for k in range(len(data)):
        newstr += newdata[k]
        u.save_file(filename, newstr) 
    print('\033[31mAll done, good job!\033[0m')
