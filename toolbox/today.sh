#!/bin/bash
# @Davesdere | David Cote | 2018 GNU GPLv3
# coding: utf-8
Now_daily=$(date +%A-%B-%d)
year=$(date +%Y)
hour=$(date +%H)
minute=$(date +%M)
amixer scontrols
amixer sset 'PCM' 90%
espeak $Now_daily
espeak $year
espeak $hour
espeak hour
espeak $minute
espeak minute
echo $Now_daily
amixer sset 'PCM' 60%
exit
