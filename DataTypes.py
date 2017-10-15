#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-14 19:45:05
# @Author  : jingray (lionel_jing@163.com)
# @Link    : http://www.jianshu.com/u/01fb0364467d
# @Version : $Id$

import os

# STRINGS
print("STRINGS")
my_string_1 = "hello"
my_string_2 = 'world'
my_multiline_string = """

Dear World,

Hello. I am a multiline python string.
I'm enclosed in triple quotes. I'd write
them here, but that would end the string!

I know! I'll use a slash as an escape character.

Triple quotes look like this: \"\"\"

Sincerely,
Python
"""
newline_character = "\n"
print(my_string_1, my_string_2)
print(my_multiline_string)
print(newline_character)
print("-----------")
print(newline_character)

# NUMBERS AND BOOLEANS
print("NUMBERS")
my_float    = 0.5
my_integer  = 7
my_negative = -3.5
my_fraction = 1/2

# what do you think THIS line of code will assign to the variable
# does_half_equal_point_five?
does_half_equal_point_five = (my_fraction == my_float)
print("The absolute value of", my_negative, "is", abs(my_negative))
print(my_integer, "squared is equal to", my_integer ** 2)
print("Does", my_fraction, "equal", my_float, "?", does_half_equal_point_five)

for left_num in range(10):
    for right_num in range(10):
        product = left_num * right_num
        print(left_num, "x", right_num, "=", product)
    print ("\n")

#List
my_list = [1, 2, 3, "a", "b", "c"]
print("my_list is:", my_list)
print("Enumerating a list...")
for i, item in enumerate(my_list):
    print("item number", i, "is", item)

print("Another way to enumerate using a list 'method'...")
for item in my_list:
    index = my_list.index(item)
    print("item", item, "has index", index)

#List Comprehensions
numbers_0_to_9 = [x for x in range(10)]
print("Numbers 0 to 9", numbers_0_to_9)

squares = [x * x for x in range(10)]
print("Squares       ", squares)

odds = [x for x in range(10) if x % 2 == 1]
print("Odds          ", odds)


# This example uses a data type called a namedtuple which is similar to a struct data type in other languages.
from collections import namedtuple
Person = namedtuple("Person", ["name", "age", "gender"])

people = [
    Person("Andy", 30, "m"),
    Person("Ping", 1, "m"),
    Person("Tina", 32, "f"),
    Person("Abby", 14, "f"),
    Person("Adah", 13, "f"),
    Person("Sebastian", 42, "m"),
    Person("Carol" , 68, "f"),
]

# first, let's show how this namedtuple works.

andy = people[0]

print("name:  ", andy.name)
print("age:   ", andy.age)
print("gender:", andy.gender)


# now let's show what we can do with a list comprehension
#
male_names = [person.name for person in people if person.gender=="m"]
print("Male names:", male_names)

teen_names = [p.name for p in people if 13 <= p.age <= 18 ]
print("Teen names:", teen_names)


# random

import random as rd

a = rd.random()
b = rd.random()
c = rd.random()
print("a is", a)
print("b is", b)
print("c is", c)
