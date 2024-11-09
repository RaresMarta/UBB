cmake_minimum_required(VERSION 3.27)
project(ADTSortedBag)

set(CMAKE_CXX_STANDARD 17)

add_executable(ADTSortedBag main.cpp
        SortedBag.cpp
        SortedBagIterator.cpp
        ExtendedTest.cpp
        ShortTest.cpp
        ShortTest.h)
