#include <exception>
#include <algorithm>
#include <iostream>
#include "IndexedList.h"
#include "ListIterator.h"


int IndexedList::removefromKtoK(int k) {  /// 0(length / k)
    k--;
    if (k < 0 || k == 0)
        throw std::exception();

    if (length < k)
        return 0;

    int nr = 0, old = k;
    while (k < length) {
        remove(k);
        k += old;
        nr++;
    }

    return nr;
}

IndexedList::IndexedList() {  /// 0(cap)
    cap = 5;
    length = 0;
    elems = new TElem[cap + 1];
    next = new int[cap + 1];
    head = -1;
    firstEmpty = 0;
    for (int i = 0; i < cap - 1; ++i)
        next[i] = i + 1;
    next[cap - 1] = -1;
}

int IndexedList::size() const {  /// 0(1)
    return length;
}

bool IndexedList::isEmpty() const {  /// 0(1)
    return length == 0;
}

TElem IndexedList::getElement(int pos) const {  /// 0(pos)
    if (pos < 0 || pos >= length) {
        std::cout << "Tried to get elem at invalid pos (getElement)" << std::endl;
        throw std::exception();
    }
    int current = head;
    for (int i = 0; i < pos; ++i)
        current = next[current];
    return elems[current];
}

TElem IndexedList::setElement(int pos, TElem e) {  /// 0(pos)
    if (pos < 0 || pos >= length) {
        std::cout << "Tried to set an element at invalid position (setElement)" << std::endl;
        throw std::exception();
    }

    int current = head;
    for (int i = 0; i < pos; ++i)
        current = next[current];

    int oldValue = elems[current];
    elems[current] = e;
    return oldValue;
}

void IndexedList::addToEnd(TElem e) {  /// 0(length)
    if (length == cap - 3)
        resize();

    int newPosition = firstEmpty;
    firstEmpty = next[firstEmpty];
    elems[newPosition] = e;
    next[newPosition] = -1;

    if (!isEmpty()) {
        int current = head;
        while (next[current] != -1) {
            current = next[current];
        }
        // current = position of last element in list
        next[current] = newPosition;
    }
    else {
        head = newPosition;
    }
    length++;
}

void IndexedList::addToPosition(int pos, TElem e) {  /// 0(pos)
    if (length == cap - 3)
        resize();

    if (pos < 0 || pos > length) {
        // std::cout << "Tried to add elem at invalid pos: " << pos << std::endl;
        // std::cout << "Current length: " << length << std::endl;
        throw std::exception();
    }

    if (pos == length) {
        addToEnd(e);
        return;
    }

    int newPosition = firstEmpty;
    if (newPosition == -1) {
        throw std::exception();
    }
    elems[newPosition] = e;
    firstEmpty = next[firstEmpty];
    length++;

    if (pos == 0) {  // Inserting at the head
        next[newPosition] = head;
        head = newPosition;
    } else {  // Inserting in the middle
        int current = head, prev = -1;
        for (int i = 0; i < pos; ++i) {
            prev = current;
            current = next[current];
        }
        next[prev] = newPosition;
        next[newPosition] = current;
    }
}

TElem IndexedList::remove(int pos) {  /// 0(pos)
    if (isEmpty()) {
        std::cout << "List is already empty" << std::endl;
        return NULL_TELEM;
    }
    if (pos < 0 || pos > length - 1) {
        throw std::out_of_range("Position " + std::to_string(pos) + " out of valid range");
    }

    int current = head, prev;
    for (int i = 0; i < pos; ++i) {
        prev = current;
        current = next[current];
    }

    TElem removedValue = elems[current];
    elems[current] = NULL_TELEM;

    if (pos == 0)
        head = next[head];
    else
        next[prev] = next[current];

    next[current] = firstEmpty;
    firstEmpty = current;

    length--;
    return removedValue;
}


int IndexedList::search(TElem e) const{  /// O(length)
    int current = head, index=0;

    while (current != -1 && elems[current] != e) {
        current = next[current];
        index++;
    }

    if (elems[current] == e)
        return index;

    return -1;
}

ListIterator IndexedList::iterator() const {  /// 0(1)
    return ListIterator(*this);
}

IndexedList::~IndexedList() {  /// O(1)
    if (elems != nullptr) {
        delete[] elems;
        elems = nullptr;
    }
    if (next != nullptr) {
        delete[] next;
        next = nullptr;
    }
    firstEmpty = 1;
    head = -1;
    length = 0;
}

void IndexedList::resize() {  /// 0(cap * 2)
    int newCap = cap * 2;
    TElem* newElems = new TElem[newCap + 1];
    int* newNext = new int[newCap + 1];

    for (int i = 0; i < cap - 1; ++i) {
        newElems[i] = elems[i];
        newNext[i] = next[i];
    }
    for (int i = cap - 1; i < newCap - 1; ++i) {
        newNext[i] = i + 1;
    }
    newNext[newCap] = -1;

    delete[] elems;
    delete[] next;

    elems = newElems;
    next = newNext;
    firstEmpty = cap - 1;
    cap = newCap;
}


