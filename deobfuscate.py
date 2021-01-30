#!/usr/bin/env python
# coding=utf-8

from numpy import random as rd

import logger as log
import err
import utils as u


def deobfuscate_code(encode, enable, id=3):
    if encode:
        if enable == True:
            dealgo(encode, enable, id)
        else:
            dealgo(encode, id)
    else:
        u.helper(err.FileIsEmpty)

def deobfuscate_file(filename, enable, save='no', id=3):
    data = u.read_file(filename)
    if data:
        res = dealgo3(data, enable)
        if save == 'yes':
            u.save_to_file(res)
    else:
        u.helper(err.NoDataRead)

def dealgo(data, enable, id):
    if id == 3:
        dealgo3(data, enable)
    elif id == 2:
        dealgo2(data, enable)
    elif id == 1:
        dealgo1(data, enable)
    else:
        u.helper(err.InputError)

def dealgo1(data, enable=False):
    pass

def dealgo2(data, enable=False):
    pass

def dealgo3(data, enable=False):
    dict = {'a': "-0_0",
            'b': "-0_1",
            'c': "-0_2",
            'd': "-0_3",
            'e': "-0_4",
            'f': "-0_5",
            'g': "-0_6",
            'h': "-0_7",
            'i': "-1_0",                
            'j': "-1_1",
            'k': "-1_2",
            'l': "-1_3",
            'm': "-1_4",
            'n': "-1_5",
            'o': "-1_6",                                
            'p': "-1_7",
            'q': "-2_0",                        
            'r': "-2_1",
            's': "-2_2",                               
            't': "-2_3",
            'u': "-2_4",                                                                                                                  
            'v': "-2_5",                                                                                                                
            'w': "-2_6",
            'x': "-2_7",
            'y': "-3_0",
            'z': "-3_1"}

    if data == None:
        u.helper(err.NoDataInput, False)

    ret = ""
    res = ""
    sign = 0

    for i in range(len(data)):
        if (i + 1) % 4 == 0:
            for j in range(sign, i+1):
                ret += str(data[j])
            u.logu(enable, ret) 

            for k, v in dict.items():
                if ret == v:
                    res += str(k)
                    u.logu(enable, k)
                                    
            u.logu(enable, res)
            sign += 4
            ret = ""

    return res
