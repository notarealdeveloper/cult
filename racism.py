#!/usr/bin/env python3

"""
    Python
    dressed like the Shell
    using ideas from Haskell
    to make a racist joke about Javascript
"""

import os
import re
import builtins
from functools import partial
import inspect
from pprint import pprint as print


def freevars(func):
    sig = inspect.signature(func)
    return {
        k:v for k,v in sig.parameters.items()
        if v.kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
    }

class list:

    def __init__(self, list):
        self.list = builtins.list(list)

    def map(self, func):
        return self.__class__([func(o) for o in self.list])

    def __iter__(self):
        return iter(self.list)

    def __repr__(self):
        return repr(self.list)


class function:

    def __new__(cls, func):
        if isinstance(func, function):
            return func
        self = object.__new__(cls)

        if not callable(func):
            value = func
            if isinstance(value, builtins.list):
                value = list(value)
            def func():
                return value

        self.func = func
        return self

    def __call__(self, *args, **kwds):
        func = partial(self.func, *args, **kwds)
        if not freevars(func):
            return func()
        else:
            return function(func)

    def __or__(self, other):
        other = function(other)
        def f(*args, **kwds):
            return other(self(*args, **kwds))
        return function(f)

    def __ror__(self, other):
        other = function(other)
        def f(*args, **kwds):
            return self(other(*args, **kwds))
        return function(f)

@function
def read(path):
    with open(path, mode='r') as fp:
        return fp.read()

@function
def grep(pattern, text):
    return list(re.finditer(pattern, text))

@function
def filter(func, it):
    return list(builtins.filter(func, it))

@function
def map(func, it):
    return list(builtins.map(func, it))

@function
def run(cmd):
    return os.popen(cmd).read()


def example_command():
    pipe = (
        'pacman -Q'
        | run
        | (lambda text: text.splitlines())
        | filter(lambda line: line.startswith('python'))
        | map(lambda line: re.sub('python', 'bird', line))
        | map(lambda line: line.split(' '))
        | (lambda pairs: {k:v for k,v in pairs})
    )
    print(pipe())


def example_readfile():
    # This works too, but you may not have any 192.* ips in your /etc/hosts
    pipe = (
        '/etc/hosts'
        | read
        | grep('.*(\d{1,3}[.]){3}\d{1,3}.*') 
        | map(lambda match: match.group())
        | filter(lambda line: line.startswith('192'))
        | map(lambda line: (re.split('[ ]+', line)))
        | (lambda pairs: {k:v for k,v in pairs})
        | (lambda dict: {v:k for k,v in dict.items()})
    )
    print(pipe())


example_command()
# example_readfile()

