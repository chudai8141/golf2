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
    def __init__(self, data, set_joint, flag_sep: bool=True):
        self.data = data
        self.joint = set_joint['j_num']
        self.joint_name = set_joint['j_name']
        self.imf = self.get_memd(self.data)
        self.result_x = None
        self.result_y = None
        self.result_z = None

        if flag_sep:
            self.sep_dim()
    
    def get_memd(self):
        self.imf = memd(self.data)

    def sep_dim(self):
        self.result_x = self.imf[:, self.joint, :]
        self.result_z = self.imf[:, self.joint+1, :]
        self.result_y = self.imf[:, self.joint+2, :]
        


class HilbertTrans:
    def __init__(self, MultEmpModeDeco):