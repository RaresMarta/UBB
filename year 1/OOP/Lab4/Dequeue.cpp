#include <deque>
#include <iostream>
#include "Dequeue.h"
#pragma once
using namespace std;

// constructor
Dequeue::Dequeue(int* array, int capacity, int size) {
    this->array = new int[capacity];
    this->capacity = capacity;
    this->size = size;
    for (int i = 0; i < size; ++i)
        this->array[i] = array[i];
}

// copy constructor
Dequeue::Dequeue(const Dequeue &other) {
    capacity = other.capacity;
    size = other.size;
    array = new int[capacity];
    for (int i = 0; i < size; ++i)
        array[i] = other.array[i];
}

// destructor
Dequeue::~Dequeue() {
    delete[] array;
    set_size(0);
}

// doubles queue capacity
void Dequeue::resize() {
    capacity *= 2;
    int* newArray = new int[capacity];

    for (int i = 0; i < size; i++)
        newArray[i] = array[i];

    delete[] array;
    array = newArray;
}


// getters and setters
int* Dequeue::get_array() const { return array; }
int Dequeue::get_capacity() const { return capacity; }
int Dequeue::get_size() const { return size; }
void Dequeue::set_array(int* newArray) { array = newArray; }
void Dequeue::set_capacity(int newCapacity) { capacity = newCapacity; }
void Dequeue::set_size(int newSize) { size = newSize; }


// queue operations
void Dequeue::push_front(TElem value) {
    if (size == capacity)
        resize();

    for (int i = size; i >= 1; i--)
        array[i] = array[i-1];

    array[0] = value;
    set_size(size + 1);
}

void Dequeue::push_back(TElem value) {
    if (size == capacity)
        resize();

    array[size] = value;
    set_size(size + 1);
}

int Dequeue::pop_front() {
    int value = array[0];
    int* newArray = new int[capacity];

    for (int i = 1; i < size; i++)
        newArray[i] = array[i];

    set_array(newArray);
    set_size(size - 1);
    return value;
}

int Dequeue::pop_back() {
    int value = array[size-1];
    int* newArray = new int[capacity];

    for (int i = 0; i < size-1; i++)
        newArray[i] = array[i];

    set_array(newArray);
    set_size(size - 1);
    return value;
}

int Dequeue::top() const {
    return array[0];
}

int Dequeue::back() const {
    return array[size - 1];
}


// overloading operations
ostream &operator<<(ostream &os, const Dequeue &deq) {
    cout << "Capacity: " << deq.capacity << endl;
    cout << "Size: " << deq.size << endl;
    for (int i = 0; i < deq.size; i++)
        cout << deq.array[i] << ' ';
    cout << endl;
}

istream &operator>>(istream &is, const Dequeue &deq) {
    // n-a sti nime'
}

Dequeue &Dequeue::operator=(const Dequeue &other) {
    if (this != &other) {
        array = other.array;
        capacity = other.capacity;
        size = other.size;
    }
    return *this;
}
