# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:44:02 2022

@author: Rahul Sharma M.Tech (Data Science)
"""
'''program to check whether the given integer is a multiple of 5'''
number = int(input("Enter an integer: "))
if(number%5==0):
    print(number, "is a multile of 5")
else:
    print(number, "is not a multiple of 5")