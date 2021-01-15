#!/usr/bin/env python
# coding=utf-8

import logger as log
#import json

def obfuscate_code(data, enable=False, id=3):
    coalgo(data, enable, id)

def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    return data

def obfuscate_file(filename, enable=False, id=3):
    data = read_file(filename)
    coalgo(data, enable, id)
    
def coalgo(data, enable, id):
    if id == 3:
        coalgo3(data, enable)
    elif id == 2:
        coalgo2(data, enable)
    else:
        coalgo1(data, enable)

def coalgo1(data, enable=False):
    for i in range(data):
        if enable == True:
            # TODO: transfer i
            log.debug(i, enable)
            if i == None:
                log.show_msg(InputError)

def coalgo2(data, enable=False):
    # TODO: a --> -0_0, h --> -0_7, i --> -1_0, p --> -1_7
    if data == None:
        log.show_msg(NoDataInput)

def coalgo3(data, enable=False):
    # TODO
    pass
