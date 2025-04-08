#!/usr/bin/env python3
import os
import re

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    # Get drive package path
    drive_share_dir = get_package_share_directory('drive')
    urdf_file_path = os.path.join(drive_share_dir, 'models', 'drive', 'urdf', 'drive.urdf')
    rviz_config_file = os.path.join(drive_share_dir, 'urdf.rviz')

    # Read and patch URDF content
    with open(urdf_file_path, 'r') as f:
        urdf_content = f.read()

    # Fix mesh paths
    urdf_content = re.sub(
        r'package://drive/meshes/',
        'package://drive/models/drive/meshes/',
        urdf_content
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'model',
            default_value='',
            description='Path to the robot model'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': urdf_content}],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        )
    ])
