#!/bin/bash
# @Davesdere | David Cote | 2018 GNU GPLv3
# coding: utf-8
## This is a simple timer script to stop the radio
echo "Timer started"
echo "This will kill a process id stored in a text file, hopefully"
echo `cat save_pid`
echo `cat timer.log`
LEN=$1
## Optimize this script with functions and hash tables
## https://www.shellscript.sh/functions.html
## https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash
sleep $LEN
kill `cat save_pid.txt`
rm save_pid.txt & rm timer.log
exit
