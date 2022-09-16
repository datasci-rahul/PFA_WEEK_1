# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:44:56 2022

@author: Rahul Sharma M.Tech (Data Science)
"""
'''program to display the given integer in reverse manner'''

number = int(input("Enter a positive integer: "))
rev = 0
while(number!=0):
    digit = number%10
    rev = (rev*10)+digit
    number = number//10
print(rev)