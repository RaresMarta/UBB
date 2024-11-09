#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>
using namespace std;


// 0(2*capacity)
void MultiMap::rehash() {
    int oldCapacity = capacity;
    capacity *= 2;
    auto *newBuckets = new Bucket[capacity];

    for (int i = 0; i < capacity; i++) {
        newBuckets[i].key = NULL_TVALUE;
        newBuckets[i].values = new TValue[5];
        newBuckets[i].capacity = 5;
        newBuckets[i].size = 0;
    }

    for (int i = 0; i < oldCapacity; i++) {
        if (buckets[i].key != NULL_TVALUE) {
            for (int j = 0; j < buckets[i].size; j++) {
                TValue v = buckets[i].values[j];
                int index = hash(buckets[i].key);

                // Use linear probing for collision handling in new array
                while (newBuckets[index].key != NULL_TVALUE && newBuckets[index].key != buckets[i].key) {
                    index = (index + 1) % capacity;
                }
                if (newBuckets[index].key == NULL_TVALUE) {
                    newBuckets[index].key = buckets[i].key;
                }
                newBuckets[index].addValue(v);
            }
        }
    }

    for (int i = 0; i < oldCapacity; i++) {
        delete[] buckets[i].values;  // Free old values array
    }
    delete[] buckets;  // Free old buckets array
    buckets = newBuckets;
}



/// Constructor - 0(TABLE_SIZE)
MultiMap::MultiMap() {
    capacity = TABLE_SIZE;
    numElems = 0;
    buckets = new Bucket[capacity];
    for (int i = 0; i < capacity; i++) {
        buckets[i].key = NULL_TVALUE;
        buckets[i].capacity = 5;
        buckets[i].size = 0;
        buckets[i].values = new TValue [buckets[i].capacity];
    }
}


/// Destructor - 0(1)
MultiMap::~MultiMap() {
    delete[] buckets;
    capacity = numElems = 0;
}


/// Hashing function - 0(1)
int MultiMap::hash(TKey key) const {
    return abs(key) % capacity;
}


/// Best - 0(1)  Worst - 0(2*capacity)
// In-built adding for bucket values
void MultiMap::Bucket::addValue(TValue v) {
    if (size >= capacity) {
        capacity *= 2;
        auto *newValues = new TValue[capacity];
        for (int i = 0; i < size; i++) {
            newValues[i] = values[i];
        }
        delete[] values;
        values = newValues;
    }
    values[size] = v;
    size++;
}


/// Best - 0(1)  Worst - 0(2*capacity)
// Add value v to bucket of key c
void MultiMap::add(TKey c, TValue v) {
    if (numElems >= loadFactor * capacity) {
        rehash();
    }
    int index = hash(c);
    int startIndex = index;
    while (buckets[index].key != NULL_TVALUE && buckets[index].key != c) {
        index = (index + 1) % capacity;
        if (index == startIndex) {
            throw std::overflow_error("HashTable is full and no suitable spot found.");
        }
    }

    if (buckets[index].key == NULL_TVALUE) {
        buckets[index].key = c;
        buckets[index].values = new TValue[5];
        buckets[index].size = 0;
        buckets[index].capacity = 5;
    }

    buckets[index].addValue(v);
    numElems++;
}



/// Best - 0(1)  Worst - 0(bucket size)
// Remove value v from bucket of key c
bool MultiMap::remove(TKey c, TValue v) {
    int index = hash(c);
    int originalIndex = index;
    bool looped = false;

    // Handle collisions using linear probing
    while (buckets[index].key != c && buckets[index].key != NULL_TVALUE) {
        index = (index + 1) % capacity;
        if (index == originalIndex) {
            looped = true;
            break;
        }
    }

    if (looped || buckets[index].key != c) {
        return false;  // Key not found or looped all the way back
    }

    // Key found, now find the value
    bool found = false;
    for (int i = 0; i < buckets[index].size; i++) {
        if (buckets[index].values[i] == v) {
            found = true;
            // Shift values to remove the current one
            for (int j = i; j < buckets[index].size - 1; j++) {
                buckets[index].values[j] = buckets[index].values[j + 1];
            }
            buckets[index].size--;
            break;
        }
    }

    if (!found) {
        return false;  // Value not found
    }

    if (buckets[index].size == 0) {
        buckets[index].key = NULL_TVALUE;  // Reset key if no values left
    }

    numElems--;  // Decrement overall number of elements
    return true;
}



/// Best - 0(1)  Worst - 0(bucket size)
// Returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty
vector<TValue> MultiMap::search(TKey c) const {
    vector<TValue> result;
    int index = hash(c);
    if (buckets[index].key == c) {  // Ensure the keys match exactly
        for (int i = 0; i < buckets[index].size; i++) {
            result.push_back(buckets[index].values[i]);
        }
    }
    return result;
}


/// 0(1)
int MultiMap::size() const {
	return numElems;
}


/// 0(1)
bool MultiMap::isEmpty() const {
	return numElems == 0;
}


/// 0(1)
MultiMapIterator MultiMap::iterator() const {
	return MultiMapIterator(*this);
}

