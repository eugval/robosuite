import numpy as np
from robosuite.models.robots.robot import Robot
from robosuite.utils.mjcf_utils import xml_path_completion, array_to_string


class Sawyer(Robot):
    """Sawyer is a witty single-arm robot designed by Rethink Robotics."""

    def __init__(self, torque=False):
        self.torque = torque
        if (torque):
            super().__init__(xml_path_completion("robots/sawyer/robot_torque.xml"))
        else:
            super().__init__(xml_path_completion("robots/sawyer/robot.xml"))

        self.bottom_offset = np.array([0, 0, -0.913])

    def set_base_xpos(self, pos):
        """Places the robot on position @pos."""
        node = self.worldbody.find("./body[@name='base']")
        node.set("pos", array_to_string(pos - self.bottom_offset))

    @property
    def dof(self):
        return 7

    @property
    def joints(self):
        return ["right_j{}".format(x) for x in range(7)]

    @property
    def links(self):
        return ["right_l{}".format(x) for x in range(7)]

    @property
    def actuators(self):
        if (self.torque):
            return ["torq_right_j{}".format(x) for x in range(7)]
        else:
            return ["vel_right_j{}".format(x) for x in range(7)]

    @property
    def init_qpos(self):
        return np.array([0, -1.18, 0.00, 2.18, 0.00, 0.57, 3.3161])

    @property
    def joint_velocity_limits(self):
        return np.array([[-1.74, 1.74],
                         [-1.328, 1.328],
                         [-1.957, 1.957],
                         [-1.957, 1.957],
                         [-3.485, 3.485],
                         [-3.485, 3.485],
                         [-4.545, 4.545]])

    @property
    def velocity_pid_gains(self):
        # return {'right_j0': {'p': 11.305, 'i': 7.033, 'd':0.1057},
        #             'right_j1': {'p': 15.561, 'i': 7.283, 'd': 0.2559},
        #             'right_j2': {'p': 12.94, 'i':3.107, 'd': 0.0005462},
        #             'right_j3': {'p': 20.675, 'i':1.491, 'd': 0.007894},
        #             'right_j4': {'p': 7.101, 'i': 1.123, 'd': 0.0007964},
        #             'right_j5': {'p': 2.129, 'i': 2.322, 'd': 0.01748},
        #             'right_j6': {'p': 2.778, 'i': 1.477, 'd':  0.00004448},
        #             }
        return {'right_j0': {'p': 78.631, 'i': 6.851, 'd':  0.0185},
                    'right_j1': {'p': 72.956, 'i': 5.038, 'd':  0.0032},
                    'right_j2': {'p': 46.062, 'i':5.444, 'd': 0.0134},
                    'right_j3': {'p': 44.857, 'i':0.119, 'd': 0.0004},
                    'right_j4': {'p': 6.431, 'i': 1.808, 'd': 0.0},
                    'right_j5': {'p':  10.188, 'i': 0.012, 'd': 0.0082},
                    'right_j6': {'p': 0.495, 'i': 1.093, 'd':  0.0},
                    }

# return {'right_j0': {'p': 5* 8.0, 'i': 0.02, 'd':  0.0001},
#                     'right_j1': {'p': 5* 7.0, 'i': 0.02, 'd':  0.0001},
#                     'right_j2': {'p': 5* 6.0, 'i': 0.02, 'd': 0.0001},
#                     'right_j3': {'p': 5* 4.0, 'i': 0.02, 'd': 0.0001},
#                     'right_j4': {'p': 5* 2.0, 'i': 0.02, 'd': 0.0001},
#                     'right_j5': {'p':  5* 0.5, 'i': 0.02, 'd': 0.0001},
#                     'right_j6': {'p': 5* 0.1, 'i': 0.02, 'd':  0.0001},
#                     }
#
