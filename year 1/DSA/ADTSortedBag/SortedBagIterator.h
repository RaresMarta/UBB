#pragma once
#include "SortedBag.h"

typedef int TComp;
class SortedBag;

class SortedBagIterator
{
    friend class SortedBag;

private:
    const SortedBag& bag;
    int current;
    int currentFreq;
    SortedBagIterator(const SortedBag& b);

public:
    TComp getCurrent() const;
    bool valid() const;
    void next();
    void first();
};

