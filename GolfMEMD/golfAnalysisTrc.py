# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:20:01 2021

@author: kimurayudai
"""

import numpy as np
import matplotlib.pyplot as plt
from MEMD_all import memd
import trc
import ht

data_name = input('data name : ')

#データの挿入
position, txt, ftr = trc.trcreader('./trc/' + data_name + '_Take_001.trc')

imf = memd(position,position.shape[1] * 2)

# setting params
frame = position.shape[1]
txt_list = list(txt[2].split())
fs_param = txt_list[0]
fs = 1 / float(fs_param)
t = np.linspace(0, fs*frame, frame)
dt = t[1] - t[0]

# trend
trend = imf[-1]

# hilbert transform
'''
this code is hilbert transform of Hip X.
if you will do hilbert transform for another positions,
please check and specify the index of other positions.
'''
# first : setting params
print('which position would you you like to choose.')
position_index = input()
position_index = int(position_index)

result = imf[:, :, position_index]
m = result.shape[0] - 1
ht_time = np.zeros((frame, m))
start = 10
end = frame - 10 
for i in range(m):
    ht_time[:, i] = np.linspace(0, frame*fs, frame)

# second : hilbert transorm
# freq : freqency, amp : amplitude
freq, amp = ht.FAhilbert(result, dt)

for i in range(m):
    plt.title('imf' + str(i+1))
    plt.xlabel('times[s]')
    plt.ylabel('freqency[Hz]')
    plt.ylim(0, 10)
    plt.scatter(ht_time[start:end, i], freq[start:end, i], s=20, c=amp[start:end, i], cmap='Blues')
    plt.colorbar()
    plt.grid(b = True)
    plt.show()


'''
flag = 1 # no trend 0

for i in range(imf.shape[0]-1):
    if flag == 0 :
        out=imf[i,:,:]
    if flag != 0 :
        out=imf[i,:,:] + imf[-1,:,:]

    #out[:,::3] = out[:,::3] + 200 * (i + 1)
    
    for j in range (int(position.shape[1]/3)):
        out[j * 3, :] = out[j * 3, :] + 1000 * (i + 1)
    out = np.hstack([ftr, out.T])
    trc.trcoutput(txt, out, "./data/golf/out/trc/" + data_name + "/IMF" + str(i+1))

out2 = imf[-1,:,:]
#out2[:,::3] = out2[:,::3] + imf.shape[0]*200
out2[::3,:] = out2[::3,:] + imf.shape[0] * 1000
out2 = np.hstack([ftr, out2.T])
trc.trcoutput(txt, out2, "./data/golf/out/trc/" + data_name + "/Trend")


#low frequncy
out3 = np.sum(imf, axis=0) 
out3[::3,:] = out3[::3,:] - imf.shape[0] * 1000
out3 = np.hstack([ftr, out3.T]) 
trc.trcoutput(txt, out3, "./data/golf/out/trc/" + data_name + "/original")
'''