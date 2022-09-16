# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:36:14 2022

@author: Rahul Sharma M.Tech (Data Science)
"""
'''Program to find Area of Triangle'''


import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(" Area of the triangle is: ", area)