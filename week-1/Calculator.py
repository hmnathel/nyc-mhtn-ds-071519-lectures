# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

class Calculator:
    def __init__(self, data):
        assert all(isinstance(x, (int, float)) for x in data), "list can only be numbers"
        self.data = data
        self.__update()
        
    def __update(self):
        self.length = len(self.data)
        self.mean = self.__calc_mean()
        self.median = self.__calc_median()
        self.variance = self.__calc_var()
        self.standev = self.__std_dev()
        
    def __calc_mean(self):
        mean = sum(self.data)/len(self.data)
        return mean
    
    def __calc_median(self):
        srt_data = sorted(self.data)
        length = len(srt_data)
        half_length = int(len(srt_data)/2)
        med_int = int((half_length)+0.5)
        if length%2 == 0:
            median = (srt_data[half_length]+srt_data[half_length-1])/2
        else:
            median = srt_data[med_int]
        return median
    
    def __calc_var(self):
        diff_square = []
        for x in self.data:
            diff_square.append((x - self.mean)**2)
        return sum(diff_square)/(len(self.data) - 1)
    
    def __std_dev(self):
        return math.sqrt(self.variance)
    
    def add_data(self, new_data):
        if type(new_data) == list:
            self.data.extend(new_data)
        else:
            self.data.append(new_data)
        self.__update()
            
    def remove_data(self, to_be_removed):
        return self.data.remove(to_be_removed)
        self.__update()
        
        
        
    
    