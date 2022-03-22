"""
Assignment: Python Modules Assignment
Program: my_definitions.py
Author: Colby Boell
Last date modified: 03/21/2022

The purpose of this program is to use modules from one file to another file and have
it work by allowing the main.py to call functions from the my_definitions.py by importing it.
"""
# imports file
import my_definitions as md

# main where we are calling are functions from the my_definitions file
if __name__ == '__main__':
    dict_list = {12: 'Colby', 13: 'Margot', 14: 'Nala'}
    set_list = ('Cardigan', 'Sweater', 'T-shirt')
    print(md.greeting())
    print(md.author())
    md.print_dict(dict_list)
    md.print_set(set_list)


