# user setting for data, impact flame
import numpy as np


impact_number = ['first_impact', 'second_impact', 'third_impact', 'fourth_impact']

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
                '../data/1111/slice_data/slice_1_Take_001.bvh',
                '../data/1111/slice_data/slice_2_Take_001.bvh',
                '../data/1111/slice_data/slice_3_Take_001.bvh',
                '../data/1111/slice_data/slice_4_Take_001.bvh'
            ]
        }

        self.straight_data = {
            'select_data' : 'straight_data',
            'first_impact' : 224,
            'second_impact' : 186,
            'third_impact' : 212,
            'fourth_impact' : 228,
            'impact_list' : [224, 186, 212, 228],
            'follor_throught' : 260,
            'data_path' : [
                '../data/1111/straight_data/straight_1_Take_001.bvh',
                '../data/1111/straight_data/straight_2_Take_001.bvh',
                '../data/1111/straight_data/straight_3_Take_001.bvh',
                '../data/1111/straight_data/straight_4_Take_001.bvh'
            ]
        }


class Sugawara:
    def __init__(self):
        self.slice_data = {
            'select_data' : 'slice_data',
            'first_impact' : 215,
            'second_impact' : 180,
            'third_impact' : 210,
            'finish' : 233,
            'data_path' : [
                '../data/sugawara/slice_data/singlePlane_slice01_Take_001.bvh',
                '../data/sugawara/slice_data/singlePlane_slice02_Take_001.bvh',
                '../data/sugawara/slice_data/singlePlane_slice03_Take_001.bvh'    
            ]
        }

        self.slice_data['impact_list'] = np.array([
            self.slice_data['first_impact'],
            self.slice_data['second_impact'],
            self.slice_data['third_impact']
            ])
        self.slice_data['min_frame'] = np.min(self.slice_data['impact_list'])
        self.slice_data['follor_throught'] = self.slice_data['finish'] - self.slice_data['min_frame']



