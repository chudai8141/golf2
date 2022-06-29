from typing import Union, List

import numpy as np
from numpy import linalg as LA

import user_setting
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

    def output_imf_bvh(self):
        pass
        

class HilbertTrans:
    def __init__(self, result_memd: MultEmpModeDeco, select_data: Union[user_setting.Kimura, user_setting.Sugawara]):
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
        print('impact - min')
        print(self.select_data[impact_number][0] - self.select_data['min_frame'])

        print('impact - follor throught')
        print(self.select_data[impact_number][1] + self.select_data['follor_throught'])
        self.freq_data = self.freq_mean[
            :Nod,
            self.select_data[impact_number] - self.select_data['min_frame'] : self.select_data[impact_number] + self.select_data['follor_throught']]
        print(len(self.freq_data[0]))

    def set_amp_data(self, Nod: int, impact_number: str):
        self.amp_data = self.amp_norm[
            :Nod,
            self.select_data[impact_number] - self.select_data['min_frame'] : self.select_data[impact_number] + self.select_data['follor_throught']]


def freq_amp_mean_norm(result_hilbert_list: List):
    freq_list = []
    amp_list = []
    for data in result_hilbert_list:
        freq_list.append(data.freq_data)
        amp_list.append(data.amp_data)
    
    freq_all_data = sum(freq_list) / len(result_hilbert_list)
    amp_all_data = sum(amp_list) / len(result_hilbert_list)
    amp_norm_data = (amp_all_data - np.min(amp_all_data)) / (np.max(amp_all_data) - np.min(amp_all_data))

    return freq_all_data, amp_norm_data

def create_spectrum_time(Nod, frame, dt):
    spectrum_time = np.zeros((Nod, frame))
    for n in range(Nod):
        spectrum_time[n, :] = np.linspace(0, dt*frame, frame)
    
    return spectrum_time
