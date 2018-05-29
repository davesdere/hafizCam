#!/bin/bash
echo "a : Accepted connection"
echo "f :Failed connection"
echo "u : User attempted connection"
echo "x : Search by"
echo "q : quit"
read -p "What do we do ? : " choice
if test "$choice" == "a"
then
    sudo cat /var/log/auth.log | grep 'Accepted'
fi
if test "$choice" == "f"
then
    sudo cat /var/log/auth.log | grep 'Failed'
fi
if test "$choice" == "u"
then
    sudo cat /var/log/auth.log | grep 'User'
fi
if test "$choice" == "q"
then
    exit
fi
if test "$choice" == "x"
then
    read -p "Enter an ip or any string: " searchFor
    sudo cat /var/log/auth.log | grep $searchFor
fi

