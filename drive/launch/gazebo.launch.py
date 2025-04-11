#!/usr/bin/env python3
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    drive_share_dir = get_package_share_directory('drive')

    # World path (make sure filename matches exactly)
    world_path = os.path.join(drive_share_dir, 'worlds', 'world.sdf')

    # URDF path
    urdf_path = os.path.join(drive_share_dir, 'models', 'drive', 'urdf', 'drive.urdf')

    return LaunchDescription([
        # Launch Ignition with your custom world
        ExecuteProcess(
            cmd=['ign', 'gazebo', '-r', world_path],
            output='screen'
        ),

        # robot_state_publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'robot_description': open(urdf_path).read()
            }],
            output='screen'
        ),

        # Spawn robot using ros_ign_gazebo
        Node(
            package='ros_ign_gazebo',
            executable='create',
            arguments=[
                '-name', 'drive',
                '-topic', 'robot_description',
                '-x', '0', '-y', '0', '-z', '0.2'
            ],
            output='screen'
        ),
    ])
