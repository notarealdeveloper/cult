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

# TODO: zsh_history
export HISTSIZE=10000
export SAVEHIST=10000
export HISTFILE=~/.zsh_history

# TODO: helper for zsh
# Several answers to this I've found so far:
# 1.`man zsh<TAB>`
# 2. zsh.pdf.

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
autoload colors && colors # load func "colors" from somewhere in $fpath and run it
# export PS1="%B$fg[red]%n$fg[white]@$fg[blue]%m $fg[magenta]%~ $fg[green]$ $fg[default]%b"
export PS1="%B${fg[red]}%n${fg[white]}@${fg[blue]}%m ${fg[magenta]}%~ ${fg[green]}$ ${fg[default]}%b"


# use emacs mode for shells(dedault)
# unfuck bunny's zsh
bindkey -e
