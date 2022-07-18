# user setting for data, impact flame
import sys

import numpy as np


impact_number = ['first_frame', 'second_frame', 'third_frame', 'fourth_frame']
user_list = ['kimura', 'sugawara', 'hishiyama']

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
        self.half_slice_data = {
            'select_data' : 'half_slice',
            'first_frame' : [233, 299],
            'second_frame' : [210, 277],
            'data_path' : [
                '../data/hishiyama/half_swing/slice_data/half_swing_first_Take_001.bvh',
                '../data/hishiyama/half_swing/slice_data/half_swing_second_Take_001.bvh'
            ]
        }
        self.half_slice_data['impact_list'] = np.array([
            self.half_slice_data['first_frame'],
            self.half_slice_data['second_frame']
        ])
        self.half_slice_data['min_impact'], self.half_slice_data['min_follor_throught'] = self.min_frame(self.half_slice_data['impact_list'])

        self.half_straight_data = {
            'select_data' : 'half_straight',
            'first_frame' : [229, 301],
            'second_frame' : [220, 298],
            'third_frame' : [193, 258],
            'fourth_frame' : [262, 334],
            'data_path' : [
                '../data/hishiyama/half_swing/straight_data/half_swing_first_Take_001.bvh',
                '../data/hishiyama/half_swing/straight_data/half_swing_second_Take_001.bvh',
                '../data/hishiyama/half_swing/straight_data/half_swing_third_Take_001.bvh',
                '../data/hishiyama/half_swing/straight_data/half_swing_fourth_Take_001.bvh'
            ]
        }
        self.half_straight_data['impact_list'] = np.array([
            self.half_straight_data['first_frame'],
            self.half_straight_data['second_frame'],
            self.half_straight_data['third_frame'],
            self.half_straight_data['fourth_frame']
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


def choice_user(user_name : str) -> object:
    if user_name == 'kimura':
        return Kimura()
    if user_name == 'sugawara':
        return Sugawara()
    if user_name == 'hishiyama':
        return Hishiyama()
    if user_name is None:
        print('choice user')
        sys.exit()

