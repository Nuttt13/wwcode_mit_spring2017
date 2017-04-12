#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 10:06:39 2017

@author: Enund
"""
#
#iteration = 0
#while iteration < 5:
#    count = 0
#    for letter in "hello, world":
#        count += 1
#    print ("Iteration " + str(iteration) + "; count: " + str(count))
#    iteration += 1

#s = "azcbobobegghakl"
#vowels = "auioe"
#count = 0
#for letter in s:
#    print(letter)
#    print(letter in vowels)
#    if letter in vowels:
#        count += 1
#print(count)

#iteration = 0
#
#while iteration < 5:
#    count = 0
#    for letter in 'hello, world':
#        count += 1
#    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
#    iteration += 1



iteration = 0

while iteration < 5:
    count = 0
    for letter in 'hello, world':
        count += 1
        if iteration % 2 == 0:
            break
    print('Iteration ' + str(iteration) + '; count is: ' + str(count))
    iteration += 1