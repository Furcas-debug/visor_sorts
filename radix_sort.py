# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 22:03:54 2020

@author: Furcas
"""
from functools import reduce
from random import shuffle
class Radix:
    def __init__(self):
        pass
    @staticmethod
    def get_num_digits(A):
        m = 0
        for item in A:
            m = max(m, item)
        return len(str(m))
    @staticmethod
    def flatten(A):
        return reduce(lambda x, y: x + y, A)
    
    def radix(self, A):
        num_digits = self.get_num_digits(A)
        for digit in range(0, num_digits):
            B = [[] for i in range(10)]
            for item in A:
                # num is the bucket number that the item will be put into
                num = item // 10 ** (digit) % 10
                B[num].append(item)
            A = self.flatten(B)
        return A
        


def main():
    arr1 = [55, 45, 3, 289, 213, 1, 288, 53, 2]
    A = Radix()
    print(A.radix(arr1))
    
    arr2  = [i for i in range(1000000)]
    
    shuffle(arr2)
    ars = Radix().radix(arr2)
    print(ars[:6], ars[-6:])

#main()