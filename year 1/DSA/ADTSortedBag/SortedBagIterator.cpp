#include "SortedBagIterator.h"
#include "SortedBag.h"
#include <exception>

using namespace std;

SortedBagIterator::SortedBagIterator(const SortedBag& b) : bag(b) {
    /// 0(1)
    current = 0;
    currentFreq = bag.data[0].freq;
}

bool SortedBagIterator::valid() const {
    /// 0(1)
    return (current >= 0 && current < bag.nrPairs && currentFreq >= 0);
}

TComp SortedBagIterator::getCurrent() const {
    /// 0(1)
    if (valid())
        return bag.data[current].elem;
    else
        throw exception();
}

void SortedBagIterator::next() {
    /// 0(1)
    if (!valid())
        throw exception();
    else {
        if (currentFreq > 1)
            currentFreq--;
        else {
            current++;
            currentFreq = bag.data[current].freq;
        }
    }
}

void SortedBagIterator::first() {
    /// 0(1)
    current = 0;
    currentFreq = bag.data[0].freq;
}

