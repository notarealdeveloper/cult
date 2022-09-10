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

# Things to do together (or individually)
#
# TODO: Make PS1 colorful. We need to understand the syntax before we deserve a colorful prompt.
# I'll set an obnoxiously minimal one for now, to force us to make it better.
export PS1='$ '

# TODO: Understand how to make zsh save history. Mine currently isn't saving anything
# with our bare bones config.

# TODO: Figure out how to figure things out. What's the best way to learn these things?
# Is it man zsh? zsh --help? Is there built-in documentation like vim? What do zsh experts
# do when they don't know what to do?
