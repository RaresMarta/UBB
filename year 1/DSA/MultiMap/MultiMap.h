#pragma once
#include<vector>
#include<utility>
//DO NOT INCLUDE MultiMapIterator

using namespace std;

//DO NOT CHANGE THIS PART
typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
#define NULL_TVALUE -111111
#define NULL_TELEM pair<int,int>(-111111, -111111)
class MultiMapIterator;

const int TABLE_SIZE = 13;

class MultiMap {
    friend class MultiMapIterator;

private:
    struct Bucket {
        TKey key;
        TValue *values;
        int capacity, size;
        void addValue(TValue v);
    };
    Bucket* buckets;
    int capacity, numElems;
    int loadFactor = 0.75;
    int hash(TKey key) const;

public:
    // Constructor
    MultiMap();

    // Destructor
    ~MultiMap();

    // Adds a key value pair to the multimap
    void add(TKey c, TValue v);

    // Removes a key value pair from the multimap
    // Returns true if the pair was removed (if it was in the multimap) and false otherwise
    bool remove(TKey c, TValue v);

    // Returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty
    vector<TValue> search(TKey c) const;

    // Returns the number of pairs from the multimap
    int size() const;

    // Checks whether the multimap is empty
    bool isEmpty() const;

    // Returns an iterator for the multimap
    MultiMapIterator iterator() const;

    void rehash();
};

