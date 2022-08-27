#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 04:22:26 2021

@author: aman
"""

def two_sums(numbers, target):
    size = len(numbers)
    first_index = 0
    last_index = 1
    s = 0
    while first_index < size:
        s = numbers[first_index] + numbers[last_index]
        if target == s:
            (a, b) = (first_index, last_index)
            return (a, b)
        elif last_index < size-1:
            last_index += 1
        else:
            last_index = first_index + 1
            first_index += 1


(index1, index2) = two_sums([1234,5678,9012], 14690)
print("(", index1, ",",index2,")")