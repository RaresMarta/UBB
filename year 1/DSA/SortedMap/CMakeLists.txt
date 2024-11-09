cmake_minimum_required(VERSION 3.28)
project(lab5)

set(CMAKE_CXX_STANDARD 17)

add_executable(lab5 main.cpp
        SortedMap.cpp
        SortedMap.h
        ShortTest.cpp
        ShortTest.h
        ExtendedTest.cpp
        ExtendedTest.h
        SMIterator.cpp
        SMIterator.h)
