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

# =======================================
# Things to do together or individually.

# TODO: This one is just for the bird.
# Refactor this file and push the changes to master.
# I want you to read all the comments I typed in here (they're a bit verbose,
# but that's ok). Once you're done reading each comment, I want you to delete
# it and replace it with one line, or a few words, so we can keep this file
# nice and concise. For example, once you've read the comment below about
# autoload and prompt colors, delete it and replace it with something more
# brief (e.g., just a heading that says "prompt colors"). You can decide
# what to type, but they should summarize what you learned from the deleted
# paragraph, if anything. Same deal for the paragraph about emacs mode vs
# vi mode and all the other big comments in this file. Refactoring is
# important, so let's delete all the Bunny's yammering and keep this file
# nice and tight.

# TODO: Understand how to make zsh save history.
# Mine currently isn't saving anything with our bare bones config.
# Open the pdf in doc/zsh.pdf and do a ctrl+f search for HISTORY
# to figure out how. Let's save the history to ~/.zsh_history,
# and save 10000 lines of the past commands we've typed.

# TODO: Figure out how to figure things out. What's the best way to learn these things?
# Is it man zsh? zsh --help? Is there built-in documentation like vim? What do zsh experts
# do when they don't know what to do?
#
# Several answers to this I've found so far:
# 1. type `man zsh<TAB>` to see all the man pages that start with zsh.
#    Doing that shows one called zshall, which seems to be all the others
#    concatenated together into a big crazy bastard file.
#    Doing a /keyword search in that man page has helped me find some things.
#
# 2. as mentioned above, the pdf in doc/zsh.pdf is nice too.

# =======================================


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


# default mode (i.e., emacs mode)
# All shells by default let you move around a line in two ways,
# which are commonly called emacs mode and vi mode. Even people
# who use vi or vim tend to use emacs mode for shells, since
# no one except extreme nerds is even aware shells have a vi
# mode at all. Apparently my zsh was getting set to vi mode
# because I export EDITOR=vim in my bashrc, and since I always
# enter zsh from within bash (bash being my default shell), this
# somehow triggered a weird behavior inside zsh of making vi mode
# my default. This may have been why for the last several years
# I've though zsh was fucked up and weird. Oh well, live and learn.
# The following line shouldn't do anything for you, unless you've
# been explicitly using vi mode in your old zsh config. If that's
# the case, we can add some lines of the form:
# if [[ $(whoami) == raven ]]; then echo "Hey little bird"; fi
# to this file. Long story short, the following line is just to
# unfuck my zsh, and it shouldn't do anything on your end, but
# if it seems to change things unpleasantly, let me know.
bindkey -e
