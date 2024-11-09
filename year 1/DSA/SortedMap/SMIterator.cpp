#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& map) : map(map), stack(new int[CAP]), stackSize(0), currentIndex(-1) {
    first();
}

SMIterator::~SMIterator() {
    delete[] stack;
}

void SMIterator::first() {
    stackSize = 0;
    traverseLeft(map.root);
    if (stackSize > 0) {
        currentIndex = stack[--stackSize];
    } else {
        currentIndex = -1;
    }
}

void SMIterator::next() {
    if (!valid()) {
        throw std::exception();
    }
    // traverse the right subtree
    if (map.nodes[currentIndex].right != -1) {
        traverseLeft(map.nodes[currentIndex].right);
    }
    if (stackSize > 0) {
        currentIndex = stack[--stackSize];
    } else {
        currentIndex = -1;
    }
}

bool SMIterator::valid() const {
    return currentIndex != -1;
}

TElem SMIterator::getCurrent() const {
    if (!valid()) {
        throw std::exception();  // Or more specific exception
    }
    TElem pair = TElem (map.nodes[currentIndex].key, map.nodes[currentIndex].value);
    return pair;
}

void SMIterator::traverseLeft(int nodeIndex) {
    while (nodeIndex != -1) {
        stack[stackSize++] = nodeIndex;
        nodeIndex = map.nodes[nodeIndex].left;
    }
}

