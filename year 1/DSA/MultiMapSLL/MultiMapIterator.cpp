#include "MultiMapIterator.h"
#include "MultiMap.h"

/// O(bucketsNr)
MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c), bucketsNr(c.bucketsNr) {
    first();
}

/// 0(1)
TElem MultiMapIterator::getCurrent() const {
    if (!valid())
        throw exception();
    TElem pair = TElem (current->key, current->values[position]);
    return pair;
}

/// 0(1)
bool MultiMapIterator::valid() const {
    return (index < bucketsNr && col.hashTable[index] != nullptr && position < current->size);
}

void MultiMapIterator::next() {
    if (!valid()) {
        throw exception();
    }

    if (position + 1 < current->size)
        position++;
    else if (current->next != nullptr) {
        current = current->next;
        position = 0;
    }
    else {
        index++;
        while (index < bucketsNr && col.hashTable[index] == nullptr)
            index++;
        if (index < bucketsNr && col.hashTable[index] != nullptr) {
            current = col.hashTable[index];
            position = 0;
        }
        else current = nullptr;
    }
}


/// O(bucketsNr)
void MultiMapIterator::first() {
    position = index = 0;
    //col.get_hashTable();
    while (index < bucketsNr && col.hashTable[index] == nullptr)
        //std::cout<<col.hashTable[index]<<std::endl,
        index++;

    //std::cout << "Found first node at index " << index << " with first value " << col.hashTable[index]->values[position] << std::endl;

    if (index < bucketsNr && col.hashTable[index] != nullptr)
        current = col.hashTable[index];
    else
        current = nullptr;
}

/*
#include "MultiMapIterator.h"
#include "MultiMap.h"
#include <iostream>

MultiMapIterator::MultiMapIterator(const MultiMap& c): col(c) {
    this->currentindex = 0;
    while (this->currentindex < c.bucketsNr+1 && c.hashTable[currentindex] == nullptr)
        currentindex++;
    if (currentindex < c.bucketsNr + 1)
        currentElem = c.hashTable[currentindex];                ///O(maxadd)
    else                                                ///Ω(1)
        currentElem = nullptr;
    currentpos = 0;
}

TElem MultiMapIterator::getCurrent() const{
    if (!valid())
        throw std::exception();
    return make_pair(this->currentElem->key, this->currentElem->values[currentpos]);  ///θ(1)
}

bool MultiMapIterator::valid() const {
    return (currentindex < col.bucketsNr+1 && col.hashTable[currentindex] != nullptr && this->currentpos < currentElem->size);
}                                       ///θ(1)

void MultiMapIterator::next() {
    if (!valid())
        throw std::exception();

    if (currentpos + 1 < currentElem->size)
        currentpos++;

    else if (currentElem->next != nullptr and currentElem->next->size != 0) {
        currentElem = currentElem->next;
        currentpos = 0;
    }

    else {
        currentindex++;
        currentpos = 0;
        while (this->currentindex < col.bucketsNr+1 && col.hashTable[currentindex] == nullptr)
            currentindex++;
        if (currentindex < col.bucketsNr+1)                        ///O(maxadd)
            currentElem = col.hashTable[currentindex];                  ///Ω(1)
        else
            currentElem = nullptr;
    }
}

void MultiMapIterator::first() {
    this->currentpos = 0;
    this->currentindex = 0;
    while (this->currentindex < col.bucketsNr+1 && col.hashTable[currentindex] == nullptr)
        currentindex++;
    if (currentindex < col.bucketsNr+1)                        ///O(maxadd)
        currentElem = col.hashTable[currentindex];                  ///Ω(1)

    else
        currentElem = nullptr;
}


 */