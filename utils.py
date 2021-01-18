#!/usr/bin/env python
# coding=utf-8

import sys
import os
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

def blank_check(s):
    if s.isspace():
        helper(err.DoNotInputBlank)
    else:
        pass

def helper(code, exit=True):
    log.show_msg(code)
    if exit:
        sys.exit()

