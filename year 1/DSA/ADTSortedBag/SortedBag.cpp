#include "SortedBag.h"
#include "SortedBagIterator.h"
#include <iostream>
using namespace std;


SortedBag::SortedBag(Relation r) {
    /// 0(1)
    this->capacity = 10;
    this->nrPairs = 0;
    this->data = new Pair[capacity];
    this->rel = r;
}

SortedBag::~SortedBag() {
    /// 0(n)
    delete[] data;
}

void SortedBag::resize() {
    /// 0(n)
    capacity *= 2;
    Pair* newData = new Pair[capacity];
    for (int i = 0; i < nrPairs; i++)
        newData[i] = data[i];
    delete[] data;
    data = newData;
}

void SortedBag::add(TComp e) {
    /// worst: 0(n); best: 0(1)
    // increase capacity if needed
    if (nrPairs == capacity - 1)  {
        resize();
    }
    // increase freq if elem exists
    if (search(e))
        data[elemIndex(e)].freq++;
    else {
        // add new elem with freq = 1
        int pos = 0;
        while (pos < nrPairs && rel(data[pos].elem, e))
            pos++;
        for (int i = nrPairs; i > pos; --i)
            data[i] = data[i - 1];
        data[pos].elem = e;
        data[pos].freq = 1;
        nrPairs++;
    }
}


bool SortedBag::remove(TComp e) {
    /// worst: O(n); best: O(1)
    if (search(e)){
        if (data[elemIndex(e)].freq > 1)
            data[elemIndex(e)].freq--;
        else {
            Pair* newData = new Pair[capacity];
            int k = 0;
            for (int j = 0; j < nrPairs; ++j)
                if (data[j].elem != e)
                    newData[k++] = data[j];
            delete[] data;
            data = newData;
            nrPairs--;
        }
        return true;
    }
    return false;
}


bool SortedBag::search(TComp elem) const {
    /// worst: O(n); best: O(1)
    // returns true if elem exists in data array
    for (int i = 0; i < nrPairs; i++)
        if (data[i].elem == elem)
            return true;
    return false;
}


int SortedBag::elemIndex(TComp elem) const {
    /// O(n)
    // returns index of elem in data array
    for (int i = 0; i < nrPairs; i++)
        if (data[i].elem == elem)
            return i;
    return -1;
}


int SortedBag::nrOccurrences(TComp elem) const {
    /// O(n)
    if (elemIndex(elem) == -1)
        return 0;
    return data[elemIndex(elem)].freq;
}


int SortedBag::get_size() const {
    /// O(n)
    int nr = 0;
    for (int i = 0; i < nrPairs; i++)
        nr += data[i].freq;
    return nr;
}


bool SortedBag::isEmpty() const {
    /// 0(1)
    return nrPairs == 0;
}


SortedBagIterator SortedBag::iterator() const {
    /// 0(1)
    return SortedBagIterator(*this);
}

