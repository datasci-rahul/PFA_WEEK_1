# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 16:44:52 2022

@author: Rahul Sharma M.Tech (Data Science)
"""
'''program to find the average of 10 numbers using while loop'''
count = 0
sum = 0.0
while(count<10):
    number = float(input("Enter a real number: "))
    count=count+1
    sum = sum+number
avg = sum/10;
print("Average is :",avg)