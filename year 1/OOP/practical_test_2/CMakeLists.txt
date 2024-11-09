cmake_minimum_required(VERSION 3.27)
project(TestPractice)

set(CMAKE_CXX_STANDARD 17)

add_executable(TestPractice main.cpp
        Vehicle.cpp
        Vehicle.h
        Car.cpp
        Car.h
        Bike.cpp
        Bike.h
        RentalAgency.cpp
        RentalAgency.h
)
