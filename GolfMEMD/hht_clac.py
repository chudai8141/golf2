#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:40:14 2021

@author: kimurayuudai
"""
from GolfMEMD.joint import Joint
from MEMD_all import memd
import  bvh
import ht
import numpy as np
from matplotlib import pyplot as plt
import os
import copy



def memd_calc(path):
    
    data, fs, text = bvh.bvhreader(path)
    data = bvh.errc(data, 3, 6)
    dt = float(fs)
    imf = memd(data)
    
    return imf, dt, text

def hilbert_transform(imf, dt, joint_list):
    freq_list = []
    amp_list = []
    for joint in joint_list:
        freq_joint = []
        amp_joint = []
        for dimension in range(3):
            # set joint index
            index = joint + dimension
            # set data for Hilbert Transform -> result
            result = imf[:, index, :]
            # Number of decomposition
            N = result.shape[0] - 1
            # frame data
            n = result.shape[1]
            # calculation hht
            freq, amp = ht.FAhilbert(result, dt)
            freq_joint.append(freq.T)
            amp_joint.append(amp.T)
        # append freq_list and amp_list 
        freq_list.append(freq_joint)
        amp_list.append(amp_joint)
    return freq_list, amp_list

    
if __name__ == '__main__':
    # data_path = '../data/1111/straight_1_Take_001.bvh'
    dir_list = os.listdir('../data/1111/')
    dir_list = sorted(dir_list)
    dir_list = [dir_name for dir_name in dir_list if dir_name != '.DS_Store']

    # impace frame
    straight_1 = 224
    straight_2 = 186
    straight_3 = 212
    straight_4 = 228
    impact_list = [straight_1, straight_2, straight_3, straight_4]
    
    j = Joint()
    # joint_list = [j.hip, j.left_shoulder, j.left_arm, j.left_fore_arm]
    joint_list = [j.hip, j.left_shoulder, j.left_arm, j.left_fore_arm]
    
    imf_list = []
    dt_list = []
    for file in dir_list:
        file_path = '../data/1111/' + file
        imf, dt, txt = memd_calc(file_path)
        imf_list.append(imf)
        dt_list.append(dt)
    # imf_list = np.array(imf_list, dtype=np.float64)
    imf_list = np.array(imf_list)

    freq_list = []
    amp_list = []
    # hht start 
    for imf_num in range(len(imf_list)):
        freq, amp = hilbert_transform(imf_list[imf_num], dt_list[imf_num], joint_list)
        freq_list.append(freq)
        amp_list.append(amp)
    
    
    # freq_listから周波数平均を取るデータをfreqで指定
    average_frequency_list = []
    for freq in freq_list:
        average_frequency = []
        # freqからjointの指定
        for joint in freq:
            joint_mean_list = []
            # jointからdimension(次元)の指定
            for dimension in joint:
                freq_mean_list = []
                # Nod means Number of decompositions -> IMFの指定
                for Nod in dimension:
                    # 分解ごとに周波数平均を取る
                    freq_mean = np.mean(Nod)
                    freq_mean_list.append(freq_mean)
                    #
                joint_mean_list.append(freq_mean_list)
                #
            joint_mean_list = np.array(joint_mean_list)
            joint_mean_list = joint_mean_list.T
            # Average in 3 axis -> 3軸方向の平均を取る．
            # 平均の計算が終了した後，average_frequency
            mean_all_axis_list = []
            for all_axis in joint_mean_list:
                mean_all_axis = np.mean(all_axis)
                mean_all_axis_list.append(mean_all_axis)

            average_frequency.append(np.array(mean_all_axis_list))
            #
        average_frequency_list.append(np.array(average_frequency))
    # average_frequency_list = np.array(average_frequency_list)
    freq_list_copy = copy.copy(average_frequency_list)

    for freq_i in freq_list_copy:
        for joint_i in freq_i:
            for Nod in joint_i:
                # get index for argmin -> Nodとaverage_frequency_listで一番誤差が小さいもののインデックスを取得する．
                idx = np.argmin(np.abs(average_frequency_list - Nod))
                print(idx)

    
    # imf, dt = memd_calc(data_path)
    # print(imf.shape)
    # print(dt)
    

# 今後実装するメソッド
def sum_imf(imf_list, impact_list, joint_list, diff_frame = 40):
    _imf = []
    for i in range(len(joint_list)): 
        _sum_imf = []
        _impact_frame = impact_list[i]
        for n in range(len(imf_list)):
            # [n, 1:7, i + 3, _impact_frame - diff_frame: _impact_frame + diff_frame]
            _sum_imf += imf_list[n][1:7][i + 3][_impact_frame - diff_frame: _impact_frame + diff_frame]
        _imf.append(_sum_imf)
    return _imf