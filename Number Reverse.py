#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:01:45 2021

@author: aman
"""
# Reverse Number

def Reverse_num(num):
    temp = num
    s = 0
    while temp > 0:
        remainder = temp % 10
        s = (10 * s) + remainder
        temp = temp//10
    return s
   
num = int(input("Enter a number to be reversed: "))
print("This is the answer:", Reverse_num(num))