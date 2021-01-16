#!/usr/bin/env python
# coding=utf-8

import logger as log


def get_key():
    # TODO: get the key mapping from cmap
    pass


def deobfuscate_code(encode, enable=False, id=3):
    if encode:
        for v in encode:
            if v == cmap[k]:
                print(cmap[k])
                if enable == True:
                    log.debug(cmap[k], enable)
                else:
                    pass
            else:
                pass
    else:
        log.show_msg(NoDataInput)

def deobfuscate_file(filename, enable=False, id=3):
    # TODO: decode the file then write into new file
    # data = dealgo(filename, enable, id)
    pass

def dealgo(filename, enable=False, id=3):
    pass
