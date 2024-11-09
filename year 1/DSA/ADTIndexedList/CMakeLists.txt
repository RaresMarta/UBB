cmake_minimum_required(VERSION 3.27)
project(ADTIndexedList)

set(CMAKE_CXX_STANDARD 17)

add_executable(ADTIndexedList main.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        IndexedList.cpp
        IndexedList.h
        ListIterator.cpp
        ListIterator.h
        ShortTest.cpp
        ShortTest.h)
