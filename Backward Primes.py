#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 18:56:28 2021

@author: aman
"""

#Backward Prime

def backwards_prime(start, stop):
    l = []
    dic = {}
    step = 2
    if start % 2 == 0:
        start = start + 1
    for i in range(start,stop+1,step):
        if i//10 != 0:
            if i in dic.values():
                l.append(i)
            elif isprime(i):
                buff = Reverse_num(i)
                if i != buff:
                    if isprime(buff):
                        l.append(i)
                        dic[i] = buff                    
    return l

def isprime(num):
    prime = True
    if num%2 == 0:
        prime = False
    else:    
        for i in range(2,int((num**(0.5))+1)):
            if num % i == 0:
                prime = False  
                break
    return prime

def Reverse_num(num):
    s = int(str(num)[::-1])
    return s
    
print(backwards_prime(2,100))
                

            