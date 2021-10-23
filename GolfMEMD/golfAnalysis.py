#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:29:43 2021

@author: dong
"""

import numpy as np
import bvh as bvh
import matplotlib.pyplot as plt
from MEMD_all import memd
from MEMD_all import wafa
from MEMD_all import hhtplot
import ht as hs

path = '../data/0914/18th_shots_Take_001.bvh'
#path = './data/golf/CMUGolf.bvh'
[data, fs, text] = bvh.bvhreader(path)

data = bvh.errc(data, 3, 6)

#data [:3,:] = 0
#up 80-220
#down 221-280  #ki 283
#follow 281-400

dt = float(fs)
imf = memd(data)
#imf = memd(data[80:])
#imf = memd(data[281 * 4: 400 * 4])

#分解後のチャンネルを選んでプロット

joints = [3,36,114,45,18,9]

for j in range(len(joints)):
    index = joints[j]
    #club 112-1
    
    #rightleg 10-1
    #leftleg 19-1
    
    #neck 37-1
    
    #RightArm 46-1
    
    #LeftArm 115-1
    
    
    
    result = imf[:,index,:] #imf corresponding to 1st component
    N = result.shape[0] + 1
    n = result.shape[1]
    t = np.linspace(0, dt*n, n)
    
    
    # 瞬時周波数と瞬時振幅を計算
    m=result.shape[0]-1
    n=result.shape[1]
    freq, amp = hs.FAhilbert(result, dt)
    freqall = freq
    ampall = amp ** 2
    #freq1, amp1 = hs.FAhilbert(result1, dt)
    #freq2, amp2 = hs.FAhilbert(result2, dt)
    
    for i in range(2):
        result = imf[:,i + index,:] #imf corresponding to 1st component
        freq, amp = hs.FAhilbert(result, dt)
        freqall = freqall + freq
        ampall = ampall + amp ** 2
    
    freqall = freqall / 3
    ampall = np.sqrt(ampall)
    
    #WAFA　スムージングを行う
    window=13
    freqall = wafa(freqall, ampall, window)
    ampall = (ampall - np.min(ampall)) /  (np.max(ampall) - np.min(ampall))
    
    #ヒルベルトスペクトラム
    #polt用時間を作る
    t2=np.zeros((n,m))
    for i in range(m):
        t2[:,i] = np.linspace(0, n * dt, n)
    
    #振幅の大きいIMFを上にする
    freqall, ampall = hhtplot(freqall, ampall)
    #スペクトラム
    plt.clf()
    plt.figure(dpi=200, figsize=(16,9))
        
    plt.rcParams["font.family"] = "Times New Roman" 
    plt.rcParams["font.size"] = 30
        
    #plt.scatter(t2, freqq, s=100, c=amp[0:n,], cmap='jet')
    for i in range(m):
        plt.scatter(t2[:,i], freqall[:,i], s=100, c=ampall[0:n,i], cmap='jet')
        plt.clim(0,1)
    ax = plt.gca()
    ax.set_facecolor([0.0,0.0,0.5])
    
    plt.ylim(0, 10)
    #plt.title("spectrum", fontsize=20)    #タイトルを付ける
    plt.xlabel('time(s)')        #x軸に名前をつける
    plt.ylabel('frequency(Hz)') #y軸に名前をつける
    plt.colorbar()
    plt.show()



flag = 0 # no trend 0

for i in range(imf.shape[0]-1):
    if flag == 0 :
        out=imf[i,:,:]
    if flag != 0 :
        out=imf[i,:,:] + imf[-1,:,:]
    out[0,:]=out[0,:] + (i+1)*150
    bvh.bvhoutput(bvh.errb(out.T, 3, 6), fs, "./data/golf/out/IMF" + str(i+1), text)

out = imf[-1,:,:]
# if flag == 0 :
#     out[0:3,:] = 0
out[0,:]=out[0,:] + imf.shape[0]*150
bvh.bvhoutput(bvh.errb(imf[-1,:,:].T, 3, 6), fs, "./data/golf/out/Trend", text)


#low frequncy
out2=np.sum(imf, axis=0) 
out2[0,:] = out2[0,:] - imf.shape[0] * 150
# out2[0,:]=0
# if flag == 0 :
#     out2[0:3,:] = 0
bvh.bvhoutput(bvh.errb(out2.T, 3, 6), fs, "./data/golf/out/original", text)

# #低周波
# for i in range(3):
#     out=np.sum(imf[-(i+2):,:,:], axis=0)
#     out[0,:] = out[0,:] + (-i + 3)*150
#     bvh.bvhoutput(bvh.errb(out.T, 3, 6), fs, "./data/golf/out/" + str(i+1), text)

# out = imf[-1,:,:]
# # if flag == 0 :
# #     out[0:3,:] = 0
# out[0,:]=out[0,:] + 4 *150
# bvh.bvhoutput(bvh.errb(imf[-1,:,:].T, 3, 6), fs, "./data/golf/out/Trend", text)
