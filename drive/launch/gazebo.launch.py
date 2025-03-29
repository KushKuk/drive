import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    drive_share_dir = get_package_share_directory('drive')
    gazebo_ros_share_dir = get_package_share_directory('gazebo_ros')

    gazebo_launch = os.path.join(gazebo_ros_share_dir, 'launch', 'gazebo.launch.py')
    empty_world = os.path.join(gazebo_ros_share_dir, 'worlds', 'empty.world')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch),
            launch_arguments={'world': empty_world}.items()
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_footprint_base',
            arguments=['0', '0', '0', '0', '0', '0', 'base_footprint', 'base_link']
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_entity',
            arguments=[
                '-file', os.path.join(drive_share_dir, 'urdf', 'drive.urdf'),
                '-entity', 'drive'
            ],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'topic', 'pub', '/calibrated', 'std_msgs/msg/Bool', '{data: true}', '--once'],
            output='screen'
        )
    ])

if __name__ == '__main__':
    generate_launch_description()
