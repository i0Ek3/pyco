#!/usr/bin/env python
# coding=utf-8

import os

import logger as log
import err
import utils as u


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

def coalgo3(data, enable=False):
    # TODO
    pass
