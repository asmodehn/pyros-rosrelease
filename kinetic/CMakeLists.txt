cmake_minimum_required(VERSION 2.8.3)
project(pyros)

# Minimal Python module setup - catkin is assumed preinstalled along with ROS
# This assume catkin is installed along with a minimal ROS system.
find_package(catkin REQUIRED COMPONENTS
    catkin_pip
)

# defining current package as a package that should be managed by pip (not catkin - even though we make it usable with workspaces)
catkin_pip_package(pyros)

## Unit tests
if (CATKIN_ENABLE_TESTING)

    ############
    # Nose Tests
    ############

    # What kind of tests could be generic
    catkin_add_pytests(tests/test_pyros_server)
    catkin_add_pytests(tests/test_pyros_client)
    catkin_add_pytests(tests/test_pyros)

endif()

