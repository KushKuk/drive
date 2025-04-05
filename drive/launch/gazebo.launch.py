#!/usr/bin/env python3
import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    urdf_path = '/home/kush/nav2_ws/src/drive/models/drive/urdf/drive.urdf'

    return LaunchDescription([
        # Launch Ignition Gazebo with empty world
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-r', 'empty.sdf'],
            output='screen'
        ),

        # Start robot_state_publisher with URDF
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'robot_description': open(urdf_path).read()
            }],
            output='screen'
        ),

        # Spawn robot in Ignition using ros_ign_gazebo
        Node(
            package='ros_ign_gazebo',
            executable='create',
            arguments=[
                '-name', 'drive',
                '-topic', 'robot_description',
                '-x', '0', '-y', '0', '-z', '0.1'
            ],
            output='screen'
        ),
    ])

