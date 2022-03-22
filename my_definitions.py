"""
Assignment: Python Modules Assignment
Program: my_definitions.py
Author: Colby Boell
Last date modified: 03/21/2022

The purpose of this program is to use modules from one file to another file and have
it work by allowing the main.py to call functions from the my_definitions.py by importing it.
"""


# function for greeting
def greeting():
    return 'Hello, nice to meet you!'


# function to tell who the author is
def author():
    return 'Author: Colby Boell'


# function to accept a dictionary and print out
def print_dict(the_dict):
    for key, value in the_dict.items():
        print(key, value)


# function that accepts a set and prints out
def print_set(the_set):
    for items in the_set:
        print(items)


