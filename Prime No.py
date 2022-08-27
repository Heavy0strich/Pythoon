#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 19:51:15 2021

@author: aman
"""

# check prime

def isprime(num):
    prime = True
    for i in range(2,num):
        if num % i == 0:
            prime = False
            
    return prime
        
num = int(input("Enter a number: "))
if isprime(num):
    print("is Prime")
else:
    print("Not Prime")