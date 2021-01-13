#!/usr/bin/env python
# coding=utf-8

import logger as log
#import json

def obfuscate_code(data, enable, id=3):
    # TODO
    pass


def read_file(filename):
    filename = input('Please input the path of filename which you want to obfuscate: ')
    f = open(filename)
    data = f.read()
    return data

def obfuscate_file(filename, enable, id=3):
    data = read_file(filename)
    coalgo(data, enable, id)
    
def coalgo(data, enable, id):
    if id == 3:
        coalgo3(data, enable)
    elif id == 2:
        coalgo2(data, enable)
    else:
        coalgo1(data, enable)

def coalgo1(data, enable):
    for i in range(data):
        if enable == True:
            # TODO: transfer i
            log.debug(i, enable)

