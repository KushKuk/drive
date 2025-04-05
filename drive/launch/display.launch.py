#!/usr/bin/env python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    # Paths inside the drive package
    drive_share_dir = get_package_share_directory('drive')
    urdf_file = os.path.join(drive_share_dir, 'models', 'drive', 'urdf', 'drive.urdf')
    rviz_config_file = os.path.join(drive_share_dir, 'urdf.rviz')

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
            parameters=[{'robot_description': open(urdf_file).read()}],
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

if __name__ == '__main__':
    generate_launch_description()
