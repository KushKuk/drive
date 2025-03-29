# drive

The **drive** package contains the robot description, meshes, launch files, and configuration for a six-wheeled rover. The URDF was originally exported from SolidWorks and has been modified for ROS 2. It includes sensor definitions (LIDAR and IMU) and unique naming for joints and links.

## Package Contents

- **urdf/**\
  Contains the main URDF file (`drive.urdf`) describing the robot structure and sensors.

- **meshes/**\
  Contains STL files for the robot's visual and collision models (e.g., base, wheels, bogies, rockers, and sensors).

- **launch/**\
  Contains ROS 2 launch files:

  - `display.launch.py`: Launches RViz2 and the joint state publisher GUI for visualization and interactive joint control.
  - `gazebo.launch.py`: Spawns the robot in Gazebo using an empty world.

- **config/**\
  Contains configuration files such as joint parameters (e.g., `joint_names_drive.yaml`).

## Prerequisites

- **ROS 2** (Humble or later)
- A working installation of Gazebo and RViz2
- Ament build system (colcon)

## Building the Package

1. **Create a ROS 2 Workspace** (if you haven't already):

   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws/src
   ```

2. **Clone or Copy the ****`drive`**** Package:**

   Place the package directory in your `src` folder.

3. **Build the Workspace:**

   ```bash
   cd ~/ros2_ws
   colcon build --symlink-install
   ```

4. **Source the Workspace:**

   ```bash
   source install/setup.bash
   ```

## Usage

### Visualize in RViz2

Launch the display file to see the robot model and interact with it using the joint state publisher GUI:

```bash
ros2 launch drive display.launch.py
```

*Tips:*

- Set the **Fixed Frame** in RViz2 (e.g., to `base_link`) to ensure proper visualization.
- If the robot model doesn't appear, verify that the `robot_state_publisher` is publishing the TF tree.

### Spawn in Gazebo

To spawn the robot in an empty Gazebo world, run:

```bash
ros2 launch drive gazebo.launch.py
```

*Notes:*

- Gazebo might take a few moments to load. If the model is not immediately visible, use the camera controls to navigate.
- Ensure your meshes and URDF file paths are correct so that Gazebo can locate the visual models.

## Mesh and URDF Path Considerations

- The URDF uses the `package://drive/meshes/` URI format to locate STL files.
- Ensure your `CMakeLists.txt` properly installs the `meshes` directory so that the files can be found when running the package.
- Avoid using absolute paths to ensure portability.

## Troubleshooting

- **RViz Model Not Displaying:**\
  Verify that the `robot_state_publisher` loaded the URDF by checking the `/robot_description` parameter and the `/tf` topics.

- **Gazebo Model Spawning Issues:**\
  Check the Gazebo console for errors. Ensure that the URDF and mesh files are correctly installed and referenced. Adjust camera controls if the model is spawned out of view.

- **Long Load Times in Gazebo:**\
  Performance might be affected by system graphics or the complexity of the model. Try a simpler world file or update your graphics drivers if needed.

## Contributing

Contributions and improvements are welcome! Please fork the repository and open pull requests with bug fixes or enhancements.

## License

This package is licensed under the BSD License.
