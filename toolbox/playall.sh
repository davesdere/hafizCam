#!/bin/bash
#### @Davesdere | David Cote | MIT License 2018
# coding: utf-8
## This plays the Music folder as a playlist with VLC for command line.
## It works on a rPi.
folder=$1
## The code without the nohup
#find ./Music/$folder -type f -exec cvlc --one-instance --playlist-enqueue --playlist-autostart -Z '{}' +
## The code with the nohup and the variable for a subfolder
#nohup find ./Music/$folder -type f -exec cvlc --one-instance --playlist-enqueue --    playlist-autostart -Z '{}' + > radio.log 2>&1 &
#sudo apt-get install vlc
nohup find ./Music/$folder -type f -exec cvlc --one-instance --playlist-enqueue --playlist-autostart -Z '{}' + > radio.log 2>&1 &
echo $! > save_pid.txt

exit
