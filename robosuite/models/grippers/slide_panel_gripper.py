"""
A version of TwoFingerGripper but always closed.
"""
import numpy as np

from robosuite.utils.mjcf_utils import xml_path_completion
from robosuite.models.grippers.gripper import Gripper

class SlidePanelGripper(Gripper):
    """
    Same as TwoFingerGripper, but always closed
    """

    def __init__(self):
        super().__init__(xml_path_completion("grippers/slide_panel_gripper.xml"))

    def format_action(self, action):
        # return np.array([0.8,-0.8]) #np.array([1, -1])
        return np.array([]) #np.array([1, -1])

    @property
    def init_qpos(self):
       #return np.array([-0.020833, 0.020833])
       return np.array([])

    @property
    def joints(self):
        return []#["r_gripper_l_finger_joint", "r_gripper_r_finger_joint"]

    @property
    def dof(self):
        return 0

    @property
    def visualization_sites(self):
        return ["grip_site", "slide_panel_centre", "grip_site_cylinder" ]

    def contact_geoms(self):
        return [
            "r_finger_g0",
            "r_finger_g1",
            "l_finger_g0",
            "l_finger_g1",
            "r_fingertip_g0",
            "l_fingertip_g0",
            "slide_panel_g"
        ]

    @property
    def left_finger_geoms(self):
        return ["l_finger_g0", "l_finger_g1", "l_fingertip_g0"]

    @property
    def right_finger_geoms(self):
        return ["r_finger_g0", "r_finger_g1", "r_fingertip_g0"]


