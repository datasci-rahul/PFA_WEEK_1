# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:44:19 2022

@author: Rahul Sharma M.Tech (Data Science)
"""
'''program to check whether the given integer is a multiple of both 5 and 7'''

number = int(input("Enter an integer: "))
if((number%5==0)and(number%7==0)):
    print(number, "is a multiple of both 5 and 7")
else:
    print(number, "is not a multiple of both 5 and 7")