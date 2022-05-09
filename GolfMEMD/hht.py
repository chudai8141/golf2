import os
import copy

import numpy as np
from numpy import linalg as LA
from matplotlib import pyplot as plt

from user import User
from MEMD_all import memd
import bvh
import ht


def get_data(data_path: str, set_joint: dict):
    data, fs, text = bvh.bvhreader(data_path)
    data = bvh.errc(data, set_joint['j_num'], set_joint['j_num']+3)
    dt = float(fs)
    return data, dt, text


class MultEmpModeDeco:
    def __init__(self, data, dt, set_joint, flag_sep: bool=True):
        self.data = data
        self.dt = dt
        self.joint = set_joint['j_num']
        self.joint_name = set_joint['j_name']
        self.get_memd()

        if flag_sep:
            self.sep_dim()
    
    def get_memd(self):
        self.imf = memd(self.data)

    def sep_dim(self):
        self.result_x = self.imf[:, self.joint, :]
        self.result_z = self.imf[:, self.joint+1, :]
        self.result_y = self.imf[:, self.joint+2, :]
        

class HilbertTrans:
    def __init__(self, result_memd: MultEmpModeDeco):
        self.result = result_memd
        self.hilbert_transform()

    def hilbert_transform(self):
        self.freq_x, self.amp_x = ht.FAhilbert(self.result.result_x, self.result.dt)
        self.freq_z, self.amp_z = ht.FAhilbert(self.result.result_z, self.result.dt)
        self.freq_y, self.amp_y = ht.FAhilbert(self.result.result_y, self.result.dt)

        self.freq_x, self.freq_z, self.freq_y = self.freq_x.T, self.freq_z.T, self.freq_y.T
        self.amp_x, self.amp_z, self.amp_y = self.amp_x.T, self.amp_z.T, self.amp_y.T

    def calc_means_norm(self):
        # calculation frequency average from freq_list and, amplitude normalize from amp_list
        self.freq_list = np.array([self.freq_x, self.freq_z, self.freq_y])
        self.amp_list = np.array([self.amp_x, self.amp_z, self.amp_y])
        self.freq_mean = np.mean(self.freq_list, axis=0)
        self.amp_norm = LA.norm(self.amp_list, axis=0)

