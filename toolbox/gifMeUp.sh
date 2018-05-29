#!/bin/bash
# Gif Me Up | David Cote 2018 MIT LICENSE
# Inspired from
## https://askubuntu.com/questions/648244/how-to-create-a-gif-from-the-command-line
#sudo apt-get install imagemagick
hour=$(date +%H)
minute=$(date +%M)
DATE=`date +%Y-%m-%d`
EXT=.gif
PATIENCE=$1
if [ -z "$PATIENCE" ]
then
    PATIENCE=1
fi

convert -delay $PATIENCE -loop 0 *.jpg $DATE$EXT
