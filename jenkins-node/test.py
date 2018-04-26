#!/usr/bin/env python

import os
import sys
import subprocess 
import logging


logging.basicConfig(format='Local Exec: %(message)s', level=logging.ERROR)

try:
    cmdName    = sys.argv.pop(1)
except IndexError as e:
    logging.error("No command provided")
    sys.exit(1) 

try:
    cmdArg   = sys.argv.pop(1)
except Exception as e:
    logging.error("No option to command provided")
    sys.exit(1)

cmdArgs  = sys.argv[1:] 

data = """ MemTotal:        4041708 kB
MemFree:         3092612 kB
MemAvailable:    3586428 kB
Buffers:            2704 kB
Cached:           750804 kB"""

pattern = ('Mem', 'Something', 'Nothing', 'MB')



def getSysVal(arg, *args):
    matchPatterns = list(args)
    fileLines = arg

    print(type(fileLines))
    print(fileLines)

    print(type(matchPatterns))
    print(matchPatterns)

    matchedLines = [x for x in fileLines if any(w in x for w in matchPatterns)]


    stdOut =  string(matchedLines)

    return stdOut




if cmdName == 'sys_value':
    cmdStdOut = getSysVal(data, pattern)
    print("%s" % cmdStdOut)

else: 
    logging.error("Unknown command")
    sys.exit(1)






