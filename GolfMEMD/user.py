import os
import copy
from typing import List, Dict

import numpy as np
import matplotlib.pyplot as plt

from joint import Joint


class User():
    
    def __init__(self, username: str, set_joint: Dict[int, str], ballistic: str, impact_list: List[int], last_frame: int):
        self.user = username
        self.joint = set_joint['j_num']
        self.joint_name = set_joint['j_name']
        self.ballistic = ballistic # ballistic -> 弾道の意味
        self.impact_list = impact_list
        self.last_frame = last_frame
        self.output(self, output_dir='output_image')
    
    def output(self, output_dir='output_image'):
        self.output_dir = output_dir
        if not os.path.isdir(self.output_dir):
            os.mkdir(self.output_dir)
        if not os.path.isdir(os.path.join(self.output_dir, self.user)):
            os.mkdir(os.path.join(self.output_dir, self.user))
        if not os.path.isdir(os.path.join(self.output_dir, self.user, self.ballistic)):
            os.mkdir(os.path.join(self.output_dir, self.user, self.ballistic))
        if not os.path.isdir(os.path.join(self.output_dir, self.user, self.ballistic, self.joint_name)):
            os.mkdir(os.path.join(self.output_dir, self.user, self.ballistic, self.joint_name))
        save_path = os.path.join(self.output_dir, self.user, self.ballistic, self.joint_name)
        print(save_path)
    
    def _update_joint(self, select_joint):
        self.joint = select_joint

    def _update_ballistic(self, ballistic):
        self.ballistic = ballistic

    def update_content(self, select_joint=None, ballistic=None):
        if select_joint is not None:
            self._update_joint(self, select_joint)
        if ballistic is not None:
            self._update_ballistic(self, ballistic)

