cmake_minimum_required(VERSION 3.13)  # CMake version check
project(Median_of_Two_Sorted_Arrays)  # Create project "Median_of_Two_Sorted_Arrays"
set(CMAKE_CXX_STANDARD 26)            # Enable c++26 standard

set(SOURCE_FILES solution.cpp)

# Add executable target with source files listed in SOURCE_FILES variable
add_executable(simple_example ${SOURCE_FILES})