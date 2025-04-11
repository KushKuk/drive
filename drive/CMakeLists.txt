cmake_minimum_required(VERSION 3.10)
project(drive)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(xacro REQUIRED)

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
install(
  DIRECTORY worlds
  DESTINATION share/${PROJECT_NAME}
)
install(
  DIRECTORY models/
  DESTINATION share/${PROJECT_NAME}/models
)

ament_package()
