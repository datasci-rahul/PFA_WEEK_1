# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:37:48 2022

@author: Rahul Sharma M.Tech (Data Science)
"""

'''program to find out the average of a set of integers'''

count = int(input("Enter the count of numbers: "))
i = 0
sum = 0
for i in range(count):
    x = int(input("Enter an integer: "))
    sum = sum + x
avg = sum/count
print(" The average is: ", avg)