#pragma once
#include <vector>
#include <iostream>
using namespace std;

typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;
typedef bool (*Condition)(TValue);

#define CAP 10000
#define NULL_TKEY (-111111)
#define NULL_TVALUE (-111111)
#define NULL_TELEM pair<int, int>(NULL_TKEY, NULL_TVALUE)

class MultiMapIterator;

class MultiMap {
    friend class MultiMapIterator;

private:
    struct Node {
        TKey key;
        TValue *values;
        int capacity, size;
        Node* next;
        void resize();
        Node(TKey k, TValue *v, int c, int s, Node* n);
        Node();
        ~Node();
    };
    Node* hashTable[CAP];
    int bucketsNr, countPairs;
    int hash(TKey k) const;

public:
    // constructor
    MultiMap();

    // destructor
    ~MultiMap();

    // adds a key value pair to the multimap
    void add(TKey k, TValue v);

    // removes a key value pair from the multimap
    // returns true if the pair was removed (if it was in the multimap) and false otherwise
    bool remove(TKey k, TValue v);

    // returns the vector of values associated to a key. If the key is not in the MultiMap, the vector is empty
    vector<TValue> search(TKey k) const;

    // returns the number of pairs from the multimap
    int size() const;

    // checks whether the multimap is empty
    bool isEmpty() const;

    // returns an iterator for the multimap
    MultiMapIterator iterator() const;

    // keeps in the MultiMap only those pairs whose values respects the given condition
    void filter(Condition cond);

    int get_bucketsNr() const;

    void get_hashTable() const;

    // creates new node on empty index
    void createNode(TKey k, TValue v, int index, Node* next);
};