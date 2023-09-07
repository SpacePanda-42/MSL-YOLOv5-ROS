import launch
import launch_ros.actions
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    yolox_ros_share_dir = get_package_share_directory('MSL_YOLO')

    webcam = launch_ros.actions.Node(
        package="v4l2_camera", executable="v4l2_camera_node",
        parameters=[
            {"image_size": [640,480]},
        ],
    )

    MSL_YOLO = launch_ros.actions.Node(
        package="MSL_YOLO", executable="MSL_YOLO",
        parameters=[
            {"view_img":True},
        ],

    )

    rqt_graph = launch_ros.actions.Node(
        package="rqt_graph", executable="rqt_graph",
    )

    return launch.LaunchDescription([
        webcam,
        MSL_YOLO,
    ])