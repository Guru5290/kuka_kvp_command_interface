import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/d/send_to_robot_ws/install/send_to_robot_v3'
