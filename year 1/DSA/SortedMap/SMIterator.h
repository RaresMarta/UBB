#pragma once
#include "SortedMap.h"
//DO NOT CHANGE THIS PART


class SMIterator {
    friend class SortedMap;

private:
    const SortedMap& map;
    int* stack;
    int stackSize;
    int currentIndex;

    void traverseLeft(int nodeIndex);

public:
    SMIterator(const SortedMap& map);
    ~SMIterator();
    void first();
    void next();
    bool valid() const;
    TElem getCurrent() const;
};