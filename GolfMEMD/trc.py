#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:37:14 2020

@author: kimurayuudai
"""
import numpy as np

def trcreader(path):
    
    with open(path, mode='r') as f:
        lists = f.readlines()
        
        for i in range(len(lists)):
            if lists[i] == '\n':
                print('nullpoint' + str(i))
                break
            
    data = 'data.txt'
    data_array = 0
    data_set = lists[:6]
    data_str = lists[i+1:]
    with open(data, mode='w') as f:
        f.writelines(data_str)
    
    data_array = np.loadtxt(data)
    #ftr = frame,times,reference
    ftr = data_array[:,:2]
    data_array = data_array[:,2:]
    
    return data_array, data_set, ftr
    
def trcoutput(txt, data, name):   
    
    datalist = []
    for i in range(data.shape[0]):
        tmp = str(int(data[i,0])) + "	"
        for j in range(1,data.shape[1] - 1):
            tmp = tmp + str(data[i,j]) + "	"
        tmp = tmp + str(data[i,-1]) + "\n"   
        datalist.append(tmp)
    
    path_w = name + '.trc'
    l = txt + datalist
    with open(path_w, mode='w') as f:
        f.writelines(l)   
