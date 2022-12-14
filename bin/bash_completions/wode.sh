#!/bin/bash

# This is arguably the paradigmatic minimal bash completion.
_wode() {
    local things=($(wode --list))
    local cur_word="${COMP_WORDS[COMP_CWORD]}"
    local prev_word="${COMP_WORDS[COMP_CWORD - 1]}"
    COMPREPLY=( $(compgen -W "${things[*]}" -- ${cur_word}) )
}
complete -F _wode wode
