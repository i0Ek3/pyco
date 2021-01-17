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
            log.show_msg(err.NoDataRead)
            sys.exit()
        else:
            return data
    else:
        log.show_msg(err.FileNotFound)

def blank_check(s):
    if s.isspace():
        log.show_msg(err.DoNotInputBlank)
        sys.exit()
    else:
        pass

