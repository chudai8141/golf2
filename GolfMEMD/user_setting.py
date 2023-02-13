# user setting for data, impact flame
import sys

import numpy as np


impact_number = ['first_frame', 'second_frame', 'third_frame', 'fourth_frame', 'fifth_frame', 'sixth_frame', 'seventh_frame', 'eighth_frame', 'ninght_frame']
user_list = ['kimura', 'sugawara', 'hishiyama', 'ikuno']

class Kimura:
    def __init__(self):
        self.slice_data = {
            'select_data' : 'slice_data',
            'first_impact' : 184,
            'second_impact' : 213,
            'third_impact' : 187,
            'fourth_impact' : 205,
            'impact_list' : [184, 213, 187, 205],
            'follor_throught' : 246,
            'data_path' : [
                './data/1111/slice_data/slice_1_Take_001.bvh',
                './data/1111/slice_data/slice_2_Take_001.bvh',
                './data/1111/slice_data/slice_3_Take_001.bvh',
                './data/1111/slice_data/slice_4_Take_001.bvh'
            ]
        }
        self.slice_data['impact_list'] = np.array([
            self.slice_data['first_impact'],
            self.slice_data['second_impact'],
            self.slice_data['third_impact'],
            self.slice_data['fourth_impact']
            ])
        self.slice_data['min_frame'] = np.min(self.slice_data['impact_list'])
        self.slice_data['follor_throught'] = self.slice_data['finish'] - self.slice_data['min_frame']


        self.straight_data = {
            'select_data' : 'straight_data',
            'first_impact' : 224,
            'second_impact' : 186,
            'third_impact' : 212,
            'fourth_impact' : 228,
            'impact_list' : [224, 186, 212, 228],
            'follor_throught' : 260,
            'data_path' : [
                './data/1111/straight_data/straight_1_Take_001.bvh',
                './data/1111/straight_data/straight_2_Take_001.bvh',
                './data/1111/straight_data/straight_3_Take_001.bvh',
                './data/1111/straight_data/straight_4_Take_001.bvh'
            ]
        }
        self.straight_data['impact_list'] = np.array([
            self.straight_data['first_impact'],
            self.straight_data['second_impact'],
            self.straight_data['third_impact'],
            self.straight_data['fourth_impact']
        ])
        self.straight_data['min_frame'] = np.min(self.straight_data['impact_list'])
        self.straight_data['follor_throught'] = self.straight_data['finish'] - self.straight_data['min_frame']

        self.select_data = {
            'straight_data' : self.straight_data,
            'slice_data' : self.slice_data
        }




class Sugawara:
    def __init__(self):
        self.user_name = 'sugawara'
        self.slice_data = {
            'select_data' : 'slice_data',
            'first_impact' : 215,
            'second_impact' : 180,
            'third_impact' : 210,
            'finish' : 233,
            'data_path' : [
                './data/sugawara/slice_data/singlePlane_slice01_Take_001.bvh',
                './data/sugawara/slice_data/singlePlane_slice02_Take_001.bvh',
                './data/sugawara/slice_data/singlePlane_slice03_Take_001.bvh'    
            ]
        }
        self.slice_data['impact_list'] = np.array([
            self.slice_data['first_impact'],
            self.slice_data['second_impact'],
            self.slice_data['third_impact']
            ])
        self.slice_data['min_frame'] = np.min(self.slice_data['impact_list'])
        self.slice_data['follor_throught'] = self.slice_data['finish'] - self.slice_data['min_frame']

        self.straight_data = {
            'select_data' : 'straight_data',
            'first_impact' : 168,
            'second_impact' : 188,
            'third_impact' : 181,
            'finish' : 233,
            'data_path' : [
                './data/sugawara/slice_data/singlePlane_slice01_Take_001.bvh',
                './data/sugawara/slice_data/singlePlane_slice02_Take_001.bvh',
                './data/sugawara/slice_data/singlePlane_slice03_Take_001.bvh'    
            ]
        }
        self.straight_data['impact_list'] = np.array([
            self.straight_data['first_impact'],
            self.straight_data['second_impact'],
            self.straight_data['third_impact']
        ])
        self.straight_data['min_frame'] = np.min(self.straight_data['impact_list'])
        self.straight_data['follor_throught'] = self.straight_data['finish'] - self.straight_data['min_frame']

        self.select_data = {
            'straight_data' : self.straight_data,
            'slice_data' : self.slice_data
        }


class Hishiyama:
    def __init__(self) -> None:
        self.user_name = 'hishiyama'

        # replace ..._impact -> ..._frame<list> [impact, frame number]
        #
        self.half_slice_data = {
            'select_data' : 'half_slice',
            'first_frame' : [199, 257],
            'second_frame' : [192, 265],
            'third_frame' : [216, 277],
            'fourth_frame' : [201, 270],
            'fifth_frame' : [215, 278],
            'sixth_frame' : [194, 272],
            'data_path' : [
                '../data/hishiyama/half_swing_2/slice_data/first_Take_001.bvh',
                '../data/hishiyama/half_swing_2/slice_data/second_Take_001.bvh',
                '../data/hishiyama/half_swing_2/slice_data/third_Take_001.bvh',
                '../data/hishiyama/half_swing_2/slice_data/fourth_Take_001.bvh',
                '../data/hishiyama/half_swing_2/slice_data/fifth_Take_001.bvh',
                '../data/hishiyama/half_swing_2/slice_data/sixth_Take_001.bvh'
            ]
        }
        self.half_slice_data['impact_list'] = np.array([
            self.half_slice_data['first_frame'],
            self.half_slice_data['second_frame'],
            self.half_slice_data['third_frame'],
            self.half_slice_data['fourth_frame'],
            self.half_slice_data['fifth_frame'],
            self.half_slice_data['sixth_frame'],
        ])
        self.half_slice_data['min_impact'], self.half_slice_data['min_follor_throught'] = self.min_frame(self.half_slice_data['impact_list'])

        self.half_straight_data = {
            'select_data' : 'half_straight',
            'first_frame' : [192, 256],
            'second_frame' : [206, 267],
            'third_frame' : [226, 301],
            'fourth_frame' : [207, 273],
            'fifth_frame' : [208, 271],
            'sixth_frame' : [183, 253],
            #              
            'data_path' : [
                '../data/hishiyama/half_swing_2/straight_data/first_Take_001.bvh',
                '../data/hishiyama/half_swing_2/straight_data/second_Take_001.bvh',
                '../data/hishiyama/half_swing_2/straight_data/third_Take_001.bvh',
                '../data/hishiyama/half_swing_2/straight_data/fourth_Take_001.bvh',
                '../data/hishiyama/half_swing_2/straight_data/fifth_Take_001.bvh',
                '../data/hishiyama/half_swing_2/straight_data/sixth_Take_001.bvh'
            ]
        }
        self.half_straight_data['impact_list'] = np.array([
            self.half_straight_data['first_frame'],
            self.half_straight_data['second_frame'],
            self.half_straight_data['third_frame'],
            self.half_straight_data['fourth_frame'],
            self.half_straight_data['fifth_frame'],
            self.half_straight_data['sixth_frame'],
        ])
        self.half_straight_data['min_impact'], self.half_straight_data['min_follor_throught'] = self.min_frame(self.half_straight_data['impact_list'])

        self.select_data = {
            'half_straight' : self.half_straight_data,
            'half_slice' : self.half_slice_data
        }

    def min_frame(self, impact_list):
        min_impact = np.min(impact_list[:, 0])
        _frame_list = np.array([
            np.abs(frame - impact) for impact, frame in impact_list
        ])
        min_follor_throught = np.min(_frame_list)
        return min_impact, min_follor_throught

class Ikuno:
    def __init__(self) -> None:
        self.user_name = 'ikuno'

        self.straight_data = {
            'select_data' : 'straight_data',
            'first_frame' : [141, 218],
            'second_frame' : [144, 221],
            'third_frame' : [142, 227],
            'fourth_frame' : [169, 245],
            'fifth_frame' : [158, 246],
            'sixth_frame' : [155, 230],
            #
            'data_path' : [
                '../data/ikuno/straight_data/straight_1_Take_001.bvh',
                '../data/ikuno/straight_data/straight_2_Take_001.bvh',
                '../data/ikuno/straight_data/straight_3_Take_001.bvh',
                '../data/ikuno/straight_data/straight_4_Take_001.bvh',
                '../data/ikuno/straight_data/straight_5_Take_001.bvh',
                '../data/ikuno/straight_data/straight_6_Take_001.bvh'
            ]
        }
        self.straight_data['impact_list'] = np.array([
            self.straight_data['first_frame'],
            self.straight_data['second_frame'],
            self.straight_data['third_frame'],
            self.straight_data['fourth_frame'],
            self.straight_data['fifth_frame'],
            self.straight_data['sixth_frame'],
        ])
        self.straight_data['min_impact'], self.straight_data['min_follor_throught'] = self.min_frame(self.straight_data['impact_list'])
        self.straight_data['top_line'] = 102

        self.headup_data = {
            'select_data' : 'headup_data',
            'first_frame' : [137, 232],
            'second_frame' : [132, 216],
            'third_frame' : [136, 220],
            'fourth_frame' : [142, 230],
            'fifth_frame' : [140, 224],
            'sixth_frame' : [136, 246],
            #
            'data_path' : [
                '../data/ikuno/slice_headup/headup_1_Take_001.bvh',
                '../data/ikuno/slice_headup/headup_2_Take_001.bvh',
                '../data/ikuno/slice_headup/headup_3_Take_001.bvh',
                '../data/ikuno/slice_headup/headup_4_Take_001.bvh',
                '../data/ikuno/slice_headup/headup_5_Take_001.bvh',
                '../data/ikuno/slice_headup/headup_6_Take_001.bvh',
            ]
        }
        self.headup_data['impact_list'] = np.array([
            self.headup_data['first_frame'],
            self.headup_data['second_frame'],
            self.headup_data['third_frame'],
            self.headup_data['fourth_frame'],
            self.headup_data['fifth_frame'],
            self.headup_data['sixth_frame'],
        ])
        self.headup_data['min_impact'], self.headup_data['min_follor_throught'] = self.min_frame(self.headup_data['impact_list'])
        self.headup_data['top_line'] = 96

        self.opening_data = {
            'select_data' : 'opening_data',
            'first_frame' : [135, 230],
            'second_frame' : [138, 236],
            'third_frame' : [140, 254],
            'fourth_frame' : [133, 226],
            'fifth_frame' : [135, 194],
            'sixth_frame' : [129, 224],
            'data_path' : [
                '../data/ikuno/slice_opening/opening_1_Take_001.bvh',
                '../data/ikuno/slice_opening/opening_2_Take_001.bvh',
                '../data/ikuno/slice_opening/opening_3_Take_001.bvh',
                '../data/ikuno/slice_opening/opening_4_Take_001.bvh',
                '../data/ikuno/slice_opening/opening_5_Take_001.bvh',
                '../data/ikuno/slice_opening/opening_6_Take_001.bvh',
            ]
        }
        self.opening_data['impact_list'] = np.array([
            self.opening_data['first_frame'],
            self.opening_data['second_frame'],
            self.opening_data['third_frame'],
            self.opening_data['fourth_frame'],
            self.opening_data['fifth_frame'],
            self.opening_data['sixth_frame'],
        ])
        self.opening_data['min_impact'], self.opening_data['min_follor_throught'] = self.min_frame(self.opening_data['impact_list'])
        self.opening_data['top_line'] = 97
        #
        self.select_data = {
            'straight_data' : self.straight_data,
            'headup_data' : self.headup_data,
            'opening_data' : self.opening_data
        }

    def min_frame(self, impact_list):
        min_impact = np.min(impact_list[:, 0])
        _frame_list = np.array([
            np.abs(frame - impact) for impact, frame in impact_list
            ])
        min_follor_throught = np.min(_frame_list)
        return min_impact, min_follor_throught


class Kurihara:
    def __init__(self):
        self.user_name = 'kurihara'

        self.straight_data = {
            'select_data' : 'straight_data',
            'first_frame' : [141, 218],
            # 'second_frame' : [144, 221],
            # 'third_frame' : [142, 227],
            # 'fourth_frame' : [169, 245],
            # 'fifth_frame' : [158, 246],
            # 'sixth_frame' : [155, 230],
            #
            'data_path' : [
                '../data/kurihara/straight_data/straight_1_Take_001.bvh' # データ追加後, つける
                # '../data/ikuno/straight_data/straight_2_Take_001.bvh',
                # '../data/ikuno/straight_data/straight_3_Take_001.bvh',
                # '../data/ikuno/straight_data/straight_4_Take_001.bvh',
                # '../data/ikuno/straight_data/straight_5_Take_001.bvh',
                # '../data/ikuno/straight_data/straight_6_Take_001.bvh'
            ]
        }
        # self.straight_data['impact_list'] = np.array([
        #     self.straight_data['first_frame'],
        #     self.straight_data['second_frame'],
        #     self.straight_data['third_frame'],
        #     self.straight_data['fourth_frame'],
        #     self.straight_data['fifth_frame'],
        #     self.straight_data['sixth_frame'],
        # ])
        # self.straight_data['min_impact'], self.straight_data['min_follor_throught'] = self.min_frame(self.straight_data['impact_list'])
        # self.straight_data['top_line'] = 102
    



def choice_user(user_name : str) -> object:
    if user_name == 'kimura':
        return Kimura()
    if user_name == 'sugawara':
        return Sugawara()
    if user_name == 'hishiyama':
        return Hishiyama()
    if user_name == 'ikuno':
        return Ikuno()
    if user_name == 'kurihara':
        return Kurihara()
    if user_name is None:
        print('choice user')
        sys.exit()

