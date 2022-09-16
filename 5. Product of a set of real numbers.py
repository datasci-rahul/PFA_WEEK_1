# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:39:46 2022

@author: Rahul Sharma M.Tech (Data Science)
"""

'''program to find the product of a set of real numbers'''

i = 0
product = 1
count = int(input("Enter the number of real numbers: "))
for i in range(count):
    x = float(input("Enter a real number: "))
    product = product * x
print("The product of the numbers is: ", product)
