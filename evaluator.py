# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:51:23 2026

@author: TIPQC
"""

print("Propositional logic evaluator for discrete math")
variables = int(input("How many variables? "))
total_combinations = 2**variables
combinations_list = [] 
for i in range(total_combinations):
    bin_equivalent = bin(i)[2:]
    while len(bin_equivalent) < variables:
        bin_equivalent = "0" + bin_equivalent
    combinations_list.append(tuple(int(val) for val in bin_equivalent))
