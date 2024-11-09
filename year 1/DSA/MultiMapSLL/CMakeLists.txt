cmake_minimum_required(VERSION 3.28)
project(MultiMapSLL)

set(CMAKE_CXX_STANDARD 17)

add_executable(MultiMapSLL main.cpp
        MultiMap.cpp
        MultiMap.h
        MultiMapIterator.cpp
        MultiMapIterator.h
        ExtendedTest.cpp
        ExtendedTest.h
        ShortTest.cpp
        ShortTest.h)
