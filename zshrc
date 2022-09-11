# Cult Curriculum
# 鸟和兔的 ~/.zshrc
#
# It's the end of the world,
# and the end is the beginning.

####################################
### To begin, this file contains ###
### nothing except what we have  ###
### built together as a couple.  ###
####################################

# add our private ~/bin directory to the $PATH
export PATH="$PATH:$HOME/bin"

# aliases
alias zrc="vim ~/.zshrc && source ~/.zshrc"
alias x='exit'
alias gs='git status'
alias gd='git diff'
alias gl='git log'

# prompt colors
# =============
# autoload uses the $fpath feature of zsh to load a function called "colors" from a
# file somewhere in the array of directories called $fpath (echo $fpath to see this).
# The "autoload" keyword in zsh seems to be a bit like the "import" or "include"
# keyword in other programming languages. As usual, importing is different from running,
# and it seems that 'autoload colors' is a bit like 'from colors import *' in python.
# Therefore, we have to run 'colors' after that, because (presumably) this may bring
# other names into scope. Note sure yet. The Bunny has never used zsh before, and he's
# figuring this out as he goes. If you know how autoload works, let me know.
autoload colors && colors
# export PS1="%B$fg[red]%n$fg[white]@$fg[blue]%m $fg[magenta]%~ $fg[green]$ $fg[default]%b"
# The above line works just fine, but I'm going to make it a bit more like the bash
# syntax for arrays, which uses ${array[key]} instead of $array[key]
export PS1="%B${fg[red]}%n${fg[white]}@${fg[blue]}%m ${fg[magenta]}%~ ${fg[green]}$ ${fg[default]}%b"


# Things to do together (or individually)

# TODO: Understand how to make zsh save history. Mine currently isn't saving anything
# with our bare bones config.

# TODO: Figure out how to figure things out. What's the best way to learn these things?
# Is it man zsh? zsh --help? Is there built-in documentation like vim? What do zsh experts
# do when they don't know what to do?
