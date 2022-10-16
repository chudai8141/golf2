from typing import Union, List

import numpy as np
from numpy import linalg as LA
from joint import Joint
from user import User

import user_setting
from MEMD_all import memd
import bvh
import ht

memd_times = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']


def get_data(data_path: str):
    data, fs, text = bvh.bvhreader(data_path)
    data = bvh.errc(data, 3, 180)
    dt = float(fs)
    return data, dt, text


class MultEmpModeDeco:
    def __init__(self, user, data, dt, text, set_joint, flag_sep: bool=True):
        self.user = user
        self.data = data
        self.dt = dt
        self.text = text
        self.joint = set_joint['j_num']
        self.joint_name = set_joint['j_name']
        self.get_memd()

        if flag_sep:
            self.sep_dim()
    
    def get_memd(self):
        self.imf = memd(self.data)
        self.Nod = self.imf.shape[0]

    def sep_dim(self):
        self.result_x = self.imf[:, self.joint, :]
        self.result_z = self.imf[:, self.joint+1, :]
        self.result_y = self.imf[:, self.joint+2, :]
    
    def update_user(self, user: User):
        self.user = user
        print('Successful update of user.')
    
    def update_joint(self, set_joint: Joint):
        past_joint = self.joint
        past_joint_name = self.joint_name
        self.joint = set_joint['j_num']
        self.joint_name = set_joint['j_name']
        print(f'before joint {past_joint}, {past_joint_name} -> update joint {self.joint}, {self.joint_name}.')
        self.sep_dim()
        print('Successful update of imf.')
        

class HilbertTrans:
    def __init__(self, result_memd: MultEmpModeDeco, select_data: Union[user_setting.Kimura, user_setting.Sugawara, user_setting.Hishiyama, user_setting.Ikuno]):
        self.result = result_memd
        self.select_data = select_data
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
        self.Nod = self.freq_mean.shape[0]
        
    def set_freq_data(self, Nod: int, impact_number: str):
        self.freq_data = self.freq_mean[
            :Nod,
            self.select_data[impact_number][0] - self.select_data['min_impact'] : self.select_data[impact_number][0] + self.select_data['min_follor_throught']]

    def set_amp_data(self, Nod: int, impact_number: str):
        self.amp_data = self.amp_norm[
            :Nod,
            self.select_data[impact_number][0] - self.select_data['min_impact'] : self.select_data[impact_number][0] + self.select_data['min_follor_throught']]


def freq_amp_mean_norm(result_hilbert_list: List):
    freq_list = []
    amp_list = []
    for data in result_hilbert_list:
        freq_list.append(data.freq_data)
        amp_list.append(data.amp_data)
    
    freq_all_data = sum(freq_list) / len(result_hilbert_list)
    amp_all_data = sum(amp_list) / len(result_hilbert_list)
    print(np.min(amp_all_data))
    print(np.max(amp_all_data))
    # amp_norm_data = (amp_all_data - np.min(amp_all_data)) / (np.max(amp_all_data) - np.min(amp_all_data))

    # return freq_all_data, amp_norm_data
    return freq_all_data, amp_all_data

def create_spectrum_time(Nod, frame, dt):
    spectrum_time = np.zeros((Nod, frame))
    for n in range(Nod):
        spectrum_time[n, :] = np.linspace(0, dt*frame, frame)
    
    return spectrum_time
