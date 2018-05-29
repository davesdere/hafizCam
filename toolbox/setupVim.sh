#!/bin/bash
#### @Davesdere | David Cote | MIT License 2018
# coding: utf-8
### Bash Script to setup my fav vim config.
## Uncomment next line to remove a config that is already in place
#rm ~/.vimrc
touch ~/.vimrc
echo "syntax enable" >> ~/.vimrc
echo "set tabstop=4" >> ~/.vimrc
echo "set shiftwidth=4" >> ~/.vimrc
echo "set expandtab" >> ~/.vimrc
echo "set number" >> ~/.vimrc
echo "filetype indent on" >> ~/.vimrc
echo "set autoindent" >> ~/.vimrc
echo "colorscheme desert" >> ~/.vimrc