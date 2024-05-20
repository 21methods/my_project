from launch import LaunchDescription
from lanch_ros.actions import Node


def generate_lanch_description():
    return LaunchDescription([
        Node(
            package='demo_node_cpp',
            executable='talker'
        )
    ])