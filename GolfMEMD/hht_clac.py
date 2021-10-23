#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:40:14 2021

@author: kimurayuudai
"""

from MEMD_all import memd
import  bvh
import ht
import numpy as np
from matplotlib import pyplot as plt


def memd_calc(path):
    
    data, fs, text = bvh.bvhreader(path)
    data = bvh.errc(data, 3, 6)
    dt = float(fs)
    imf = memd(data)
    
    return imf, dt

def hilbert_transform(imf, dt, joint:int):
    
    result = imf[:, joint, :]
    N = result.shape[0] + 1
    n = result.shape[1]
    t = np.linspace(0, dt*n, n)
    
    m = result.shape[0] - 1
    n = result.shape[1]
    freq, amp = ht.FAhilbert(result, dt)
    