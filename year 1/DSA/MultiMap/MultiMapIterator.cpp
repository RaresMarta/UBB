#include "MultiMapIterator.h"
#include <exception>

// Constructor
MultiMapIterator::MultiMapIterator(const MultiMap& mm) : multimap(mm), currentBucketIndex(-1), currentValueIndex(-1) {
    first();  // Sets the iterator to the first valid element
}

// Set iterator to the first valid element
void MultiMapIterator::first() {
    for (int i = 0; i < multimap.capacity; i++) {
        if (multimap.buckets[i].key != NULL_TVALUE && multimap.buckets[i].size > 0) {
            currentBucketIndex = i;
            currentValueIndex = 0;
            return;
        }
    }
    currentBucketIndex = -1; // No valid element found
    currentValueIndex = -1;
}

// Returns true if the iterator is positioned within the valid range
bool MultiMapIterator::valid() const {
    return currentBucketIndex != -1 && currentValueIndex != -1;
}

// Move to the next element
void MultiMapIterator::next() {
    if (!valid()) {
        throw std::exception(); // Iterator out of range
    }

    // Try to move to the next value in the same bucket
    if (currentValueIndex + 1 < multimap.buckets[currentBucketIndex].size) {
        currentValueIndex++;
    } else {
        // Move to the next bucket with a valid key and at least one value
        currentBucketIndex++;
        while (currentBucketIndex < multimap.capacity &&
        (multimap.buckets[currentBucketIndex].key == NULL_TVALUE || multimap.buckets[currentBucketIndex].size == 0)) {
            currentBucketIndex++;
        }
        if (currentBucketIndex < multimap.capacity) {
            currentValueIndex = 0;
        } else {
            currentBucketIndex = -1; // No more valid buckets
            currentValueIndex = -1;
        }
    }
}

// Get the current element
TElem MultiMapIterator::getCurrent() const {
    if (!valid()) {
        throw std::exception(); // Iterator out of range
    }
    TKey key = multimap.buckets[currentBucketIndex].key;
    TValue value = multimap.buckets[currentBucketIndex].values[currentValueIndex];
    return TElem(key, value);
}
