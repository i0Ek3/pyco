#!/usr/bin/env python
# coding=utf-8

import sys
import os
import time
import string

import logger as log
import err


def read_file(filename):
    if os.path.exists(filename):
        f = open(filename, 'r')
        data = f.read()
        f.close()
        
        """
        {debug}
        log.line(20, '+')
        print(data)
        log.line(20, '+')
        """
        return data

def is_python_file(filename):
    f = open(filename, 'r')
    first_line = f.readline()
    astr = '#!/usr/bin/env python' 
    if astr not in first_line:
        return False
    return True

def save_file(filename, data):
    f = open(filename, 'a')
    f.write(data)
    f.close()

def blank_check(s):
    if s[0].isspace():
        helper(err.DoNotInputBlank)
    else:
        pass

def helper(code, exit=True):
    log.show_msg(code)
    if exit:
        sys.exit()

def processing_bar(content):
    i = 0
    while i < 1:
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]
        i = i + 1

def is_none(data):
    if data:
        return False
    return True

def file_check(filename):
    return os.path.exists(filename)

def true_or_false(tof):
    if tof == "True":
        return True
    else:
        return False

def logu(enable, ret):
    if enable == True:
        log.debug(ret)

def save_to_file(data, filename):
    if data:
        name = "de_" + filename
        f = open(name, 'w')
        f.write(data)
        f.close()
    else:
        helper(err.NoDataRead)
