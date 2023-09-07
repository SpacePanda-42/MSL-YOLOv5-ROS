import launch
import launch_ros.actions
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    yolox_ros_share_dir = get_package_share_directory('MSL_YOLO')

    MSL_YOLO = launch_ros.actions.Node(
        package="MSL_YOLO", executable="MSL_YOLO",
        parameters=[
            {"view_img":True},
        ],

    )

    return launch.LaunchDescription([
        MSL_YOLO,
    ])