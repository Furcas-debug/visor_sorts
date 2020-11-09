# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:33:59 2020

@author: Furcas
"""


class Shell_sort:
    
    
    def __init__(self, data):
        self.data = data
    
    
    def shell_sort(self):
        """

        Parameters
        ----------
        self.data : List[int]
            DESCRIPTION.

        Returns
        -------
        List[int]
            DESCRIPTION.

        """
        last_index = len(self.data) - 1
        step = len(self.data)//2
        while step > 0:
            for i in range(last_index):
                j = i + step
                if j > last_index:
                    break
                if self.data[i] > self.data[j]:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
            step //= 2
        return self.data
    
    
'''   
arr = [4,5,3,4,8,4,6,33,93]

sort = Shell_sort(arr)

print(sort.shell_sort())
'''