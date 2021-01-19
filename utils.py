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
        if not data:
            helper(err.NoDataRead)
        else:
            return data
    else:
        helper(err.FileNotFound, False)

def is_python_file(filename):
    f = open(filename, 'r')
    first_line = f.readline()
    if '#!/usr/bin/env python' not in first_line:
        return False
    return True

def save_file(filename, data):
    f = open(filename, 'x')
    f.write(data)
    f.close()

def blank_check(s):
    if s.isspace():
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
