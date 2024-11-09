#pragma once
#include "MultiMap.h"

class MultiMap;

class MultiMapIterator {
    friend class MultiMap;

private:
    const MultiMap& multimap;
    int currentBucketIndex;
    int currentValueIndex;

public:
    MultiMapIterator(const MultiMap& mm);

    TElem getCurrent() const;
    bool valid() const;
    void next();
    void first();
};
