#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:28:30 2020

@author: dong
"""
import numpy as np
#BVH import
########################
# =============================================================================

def bvhreader(path):    
    f = open(path)
    with open(path) as f:
        l = f.readlines()
        #print(type(s))
        #print(l)
    
    for i in range (len(l)):
        if l[i]== "MOTION\n" :
            datanum=i
            break
    
    fs=l[datanum+2]
    fs=fs[12:]
    
    path_w = 'data.dat'
    s = l[datanum+3:] 
    
    with open(path_w, mode='w') as f:
        f.writelines(s)
    
    f.close()
    a = np.loadtxt('data.dat')

    return(a,fs,l[:datanum+1])
# =============================================================================

#BVH output
########################
# =============================================================================

def bvhoutput(data, fs, name, l):   
    
    path_w = name + '.bvh'
      
    np.savetxt(path_w, data, delimiter=' ')
    
    f = open(path_w)
    with open(path_w) as f:
        ls = f.readlines()
   
    n = data.shape[0];
    
    tmp1 = "Frames: " + str(n)  + "\n"
    tmp2 = "Frame Time: " + str(fs)
    lists = []
    lists.append(tmp1)
    lists.append(tmp2)
    l=l+ lists + ls
    
    with open(path_w, mode='w') as f:
        f.writelines(l)
    
    
# =============================================================================
#Error change
########################

def errc(data,strt,end):   
    
    n=data.shape[0]
    for j in range(strt, end):
        for i in range(n-1):
            if data[i,j]-data[i+1,j]<-350:
               data[i+1:,j]=data[i+1:,j]-360
            if data[i,j]-data[i+1,j]>350:
               data[i+1:,j]=data[i+1:,j]+360
    return(data)


def errb(data,strt,end):
    
    n=data.shape[0]
    for j in range(strt, end):
        for i in range(n):
            if data[i,j]<-180:
               data[i:,j]=data[i:,j]+360
            if data[i,j]>180:
               data[i:,j]=data[i:,j]-360

    return(data)



