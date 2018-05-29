#!/bin/bash
hour=$(date +%H)
minute=$(date +%M)
amixer scontrols
amixer sset 'PCM' 90%
espeak $hour
espeak $minute
amixer sset 'PCM' 60%
echo $hour:$minute
exit
