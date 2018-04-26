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



def getPath(arg):
    stdOut = subprocess.check_output("readlink -f $(which " +  arg + ")", shell=True).rstrip()
    return stdOut

def getEnvVar(arg):
    stdOut = os.environ[arg]
    return stdOut

def getSysVal(arg, *args):
#    matchPatterns = tuple(args)
    matchPatterns = ('MemAvailable', 'two', 'three')
    print(type(matchPatterns))
    print(matchPatterns)

    with open(arg, 'r') as f:
       fileLines = f.read().split('\n')
    print(type(fileLines))
    print(fileLines)

    matchedLines = [x for x in fileLines if any(w in x for w in matchPatterns)]
#    matchedLines = []
#    for l in fileLines:
#        print("Checking: " + l)
#        if any(xs in l for xs in matchPatterns):
#            matchedLines.append(l)
#
    print("Done")
    print(matchedLines)
    stdOut =  matchedLines
    return stdOut


if cmdName == 'real_path':
    cmdStdOut = getPath(cmdArg)
    print("%s" % cmdStdOut)

elif cmdName == 'env_var':
    cmdStdOut = getEnvVar(cmdArg)
    print("%s" % cmdStdOut)

elif cmdName == 'sys_value':
    cmdStdOut = getSysVal(cmdArg, cmdArgs)
    print("%s" % cmdStdOut)

else: 
    logging.error("Unknown command")
    sys.exit(1)






#    """
#     Very Simple COMMAND reference
#    
#      "real_path"
#       USAGE: [path], path
#         path, java
#         path, ansible
#    
#      "env_var"
#        USAGE: [env_var], variable_name
#          env_var, HOME
#          env_var, LANG
#          env_var, PATH
#    
#      "sys_value" (reads proc, sys, etc)
#       USAGE: [sys_value], path, attribute
#         value, /proc/meminfo, MemFree 
#         value, /sys/devices/system/cpu/vulnerabilities/meltdown, Mitigation
#         value, /etc/java/java.conf, JAVA_HOME
#        
#      "system_stat"
#       USAGE: [system], command (all comments and whitespace are removed and a list of arrays returned)
#         system, uptime
#         system, load
#        
#    
#      "any" (all comments and whitespace are removed and a list of arrays returned)
#       USAGE: [any], cmd, arg1, arg2 ...
#         any, uname, -r
#         any, free, -h
#        
#    """
#



#                                     EXTRA REFERENCE
#######################################################################################
# cmd = "ps -A|grep 'process_name'"
# ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
# output = ps.communicate()[0]
# print output


# ls_lines = subprocess.check_output(['ls', '-l']).splitlines()



# import subprocess
# child = subprocess.Popen('command',stdout=subprocess.PIPE,shell=True)
# output = child.communicate()[0]




# import platform
# platform.uname()
# ('Linux', 'fedora.echorand', '3.7.4-204.fc18.x86_64', '#1 SMP Wed Jan 23 16:44:29 UTC 2013', 'x86_64')
# 
# platform.uname().system
# 'Linux'
# 
# platform._supported_dists
# ('SuSE', 'debian', 'fedora', 'redhat', 'centos', 'mandrake',
# 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo',
# 'UnitedLinux', 'turbolinux')
#




# fcntl.fcntl(
#     proc.stdout.fileno(),
#     fcntl.F_SETFL,
#     fcntl.fcntl(proc.stdout.fileno(), fcntl.F_GETFL) | os.O_NONBLOCK,
# )
# and then using select to test if the data is ready
# 
# while proc.poll() == None:
#     readx = select.select([proc.stdout.fileno()], [], [])[0]
#     if readx:
#         chunk = proc.stdout.read()
#         print chunk
# 
# 

 
