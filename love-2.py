#!/usr/bin/env python3

class Love:

    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return f"{self.__class__.__name__}({self.type})"


class Longings(dict):
    pass


class Offerings(set):
    pass

class Person:

    def __init__(self, name, longings, offerings):
        self.name = name
        self.longings = longings
        self.offerings = offerings

    def __repr__(self):
        return f"{self.name}"


jing = Person(
    name = 'jing',
    longings = Longings({
        'teacher': 0.25,
        'father': 0.25,
        'husband': 0.25,
        'undefined': 0.25,
    }),
    offerings = Offerings({
        'ok with bunnies',
        'wont leave',
        'nerdy',
        'student',
        'extremely N',
        'likes cats',
        'kinda disorganized',
        'high pitched voice',
        'naturally monogamous',
        'the kind of girl who wears plaid',
        'the kind of girl who feels sad',
        'the kind of girl who needs a dad',
    })
)

jason = Person(
    name = 'jason',
    longings = Longings({
        'ok with bunnies': 0.90,
        'wont leave': 0.09,
        'nerdy': 0.001,
        'student': 0.001,
        'extremely N': 0.001,
        'naturally monogamous': 0.001,
        'the kind of girl who wears plaid': 0.001,
        'the kind of girl who feels sad': 0.001,
        'the kind of girl who needs a dad': 0.001,
        'the kind of girl who expresses affection': 0.001,
        'the kind of girl who expresses gratitude': 0.001,
        'anal': 0.001,
    }),
    offerings = Offerings({
        'husband',
        'father',
        'teacher',
        'forgiving',
        'wont leave',
        'old',
        'bald',
        'money i guess',
    })
)

s_jason = Person(
    name = 'monogamous jason before age 28 (deceased)',
    longings = Longings({
        'can match me in conversations about philosophy': 0.05,
        'can match me in conversations about mathematics': 0.05,
        'can match me in conversations about physics': 0.05,
        'can match me in conversations about computing': 0.05,
        'can match me in conversations about evolutionary biology': 0.05,
        'can match me in conversations about neuroscience and psychology': 0.05,
        'can match me in conversations about ayn rand': 0.05,
        'can match me in introversion so she doesnt always want to go to parties': 0.05,
        'can match me in abstraction and creative waffley bullshit in writing and speech': 0.05,
        'can match me in openness to experience': 0.05,
        'reads at least like half as much as i do': 0.05,
        'writes at least like half as much as i do': 0.05,
        'says yes at least like half as much as i do': 0.05,
        'unconditionally down with filming sex, remote or local': 0.05,
        'unconditionally down for sex outside in public usually at night': 0.05,
        'unconditionally down for anal and all its variations': 0.05,
        'as sexually inexperienced as possible (before we met)': 0.05,
        'as young as possible (before we met)': 0.05,
        'as alone as possible (before we met)': 0.05,
        'as sad as possible (before we met)': 0.05,
    }),
    offerings = Offerings({
        "i dunno, i offer the same stuff i want, we're a team",
    })
)

