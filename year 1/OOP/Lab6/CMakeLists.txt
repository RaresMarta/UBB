cmake_minimum_required(VERSION 3.27)
project(Lab6)

set(CMAKE_CXX_STANDARD 17)

add_executable(Lab6 main.cpp
        Vehicle.cpp
        Vehicle.h
        Car.cpp
        Car.h
        Truck.cpp
        Truck.h
        Garage.cpp
        Garage.h)
