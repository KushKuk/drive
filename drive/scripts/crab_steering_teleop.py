#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64

import math

class CrabTeleopNode(Node):
    def __init__(self):
        super().__init__('crab_steering_teleop')

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10)

        self.steering_publishers = [
            self.create_publisher(Float64, f'/steer_joint_{i}_controller/command', 10)
            for i in range(6)
        ]
        self.drive_publishers = [
            self.create_publisher(Float64, f'/wheel_joint_{i}_controller/command', 10)
            for i in range(6)
        ]

    def cmd_vel_callback(self, msg: Twist):
        vx = msg.linear.x
        vy = msg.linear.y

        # Calculate the crab steering angle (same for all wheels)
        if vx == 0.0 and vy == 0.0:
            angle = 0.0
        else:
            angle = math.atan2(vy, vx)

        # Calculate magnitude of velocity to apply to wheels
        speed = math.hypot(vx, vy)

        steer_msg = Float64()
        steer_msg.data = angle

        drive_msg = Float64()
        drive_msg.data = speed

        # Publish to all 6 wheels
        for pub in self.steering_publishers:
            pub.publish(steer_msg)
        for pub in self.drive_publishers:
            pub.publish(drive_msg)

def main(args=None):
    rclpy.init(args=args)
    node = CrabTeleopNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
