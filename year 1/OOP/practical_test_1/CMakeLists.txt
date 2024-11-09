cmake_minimum_required(VERSION 3.27)
project(practical_test)

set(CMAKE_CXX_STANDARD 17)

add_executable(practical_test main.cpp
        Duration.cpp
        Duration.h
        Song.cpp
        Song.h)
