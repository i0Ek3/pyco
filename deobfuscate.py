#!/usr/bin/env python
# coding=utf-8

import logger as log
import err
import utils as u


def get_key():
    # TODO: get the key mapping from cmap
    pass

def deobfuscate_code(encode, enable=False, id=3):
    if encode:
        # TODO: transfer encode to decode
        if enable == True:
            dealgo(encode, enable, id)
            # TODO: rewrite debug
            log.debug(str(encode), enable)
        else:
            dealgo(encode, enable, id)
    else:
        log.show_msg(err.NoDataInput)

def deobfuscate_file(filename, enable=False, id=3):
    data = u.read_file(filename)
    if data:
        dealgo(data, enable, id)
    else:
        log.show_msg(err.NoDataRead)

def dealgo(data, enable, id):
    if id == 3:
        dealgo3(data, enable)
    elif id == 2:
        dealgo2(data, enable)
    elif id == 1:
        dealgo1(data, enable)
    else:
        log.show_msg(err.InputError)
        sys.exit()

def dealgo1(data, enable=False):
    pass

def dealgo2(data, enable=False):
    pass

def dealgo3(data, enable=False):
    if is_standard_mode(data):
        # TODO: transfer
        pass
    else:
        log.show_msg(err.UnknownMode)

def is_standard_mode(data):
    # TODO: check data if belong to encode
    return True
