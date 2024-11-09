#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <exception>
#include <iostream>

/// 0(1)
int MultiMap::hash(TKey k) const {
    return abs(k) % bucketsNr;
}

/// 0(1)
MultiMap::Node::Node() {
    key = NULL_TKEY;
    values = nullptr;
    next = nullptr;
    capacity = 1;
    size = 0;
}

/// 0(1)
MultiMap::Node::Node(TKey k, TValue *v, int c, int s, Node *n) {
    key = k;
    values = v;
    capacity = c;
    size = s;
    next = n;
}

/// 0(1)
MultiMap::Node::~Node() {
    delete[] values;
    key = NULL_TKEY;
    capacity = size = 0;
}

void MultiMap::Node::resize() {
    auto *newValues = new TValue [capacity * 2];
    for (int i = 0; i < size; ++i) {
        newValues[i] = values[i];
    }
    delete[] values;
    values = newValues;
    capacity *= 2;
}

/// 0(bucketsNr)
MultiMap::MultiMap() {
    bucketsNr = CAP;
    countPairs = 0;
    for (int i = 0; i < bucketsNr; ++i)
        hashTable[i] = nullptr;
}

/// 0(bucketsNr)
MultiMap::~MultiMap() {
    for (int i = 0; i < bucketsNr; ++i) {
        Node* current = hashTable[i];
        while (current) {
            Node* current_copy = current;
            current = current->next;
            delete current_copy;
        }
    }
}

void MultiMap::createNode(TKey k, TValue v, int index, Node* next) {
    auto *newValues = new TValue [5];
    newValues[0] = v;
    Node *newNode = new Node(k, newValues, 5, 1, next);
    hashTable[index] = newNode;
}

void MultiMap::add(TKey k, TValue v) {
    int index = hash(k);

    // if bucket is empty create new node
    if (hashTable[index] == nullptr)
        createNode(k, v, index, nullptr);

    else {
        // traverse the SLL to find the key
        Node *current = hashTable[index];
        while (current != nullptr && current->key != k)
            current = current->next;

        if (current) {
            // if key in bucket add value to the end of array of values
            if (current->size >= current->capacity) {
                current->resize();
            }
            current->values[current->size] = v;
            current->size++;
        }
        else {
            // key does not exist, insert at the beginning of SLL
            createNode(k, v, index, hashTable[index]);
        }
    }
    countPairs++;
}

bool MultiMap::remove(TKey k, TValue v) {
    int index = hash(k);
    // if key not in hashtable return false
    if (hashTable[index] == nullptr)
        return false;

    // search for key in SLL
    Node *current = hashTable[index];
    Node *prev = nullptr;
    while (current != nullptr && current->key != k) {
        prev = current;
        current = current->next;
    }

    if (current && current->key == k) {
        // key was found
        if (current->size == 1 && current->values[0] == v) {
            // node will be empty so it needs to be removed
            if (prev == nullptr)
                hashTable[index] = current->next;
            else
                prev->next = current->next;
            delete current;
            countPairs--;
            return true;
        }
        else if (current->size > 1){
            // search for value in vector
            for (int i = 0; i < current->size; ++i) {
                if (current->values[i] == v) {
                    // value was found
                    for (int j = i; j < current->size - 1; ++j)
                        current->values[j] = current->values[j + 1];
                    current->size--;
                    countPairs--;
                    return true;
                }
            }
        }
    }
    return false;
}


/// 0(size of node)
vector<TValue> MultiMap::search(TKey k) const {
    vector<TValue> values;
    int index = hash(k);
    // if bucket is empty return empty vector
    if (hashTable[index] == nullptr)
        return values;

    // traverse the SLL to find the node with given key
    Node* current = hashTable[index];
    while (current != nullptr && current->key != k)
        current = current->next;

    // if the key is found then fill the vector with its values
    if (current) {
        for (int i = 0; i < current->size; ++i)
            values.push_back(current->values[i]);
    }
    return values;
}

/// 0(1)
int MultiMap::size() const {
    return countPairs;
}

/// 0(1)
bool MultiMap::isEmpty() const {
    return countPairs == 0;
}

MultiMapIterator MultiMap::iterator() const {
    return MultiMapIterator(*this);
}

/// 0(bucketsNr)
void MultiMap::filter(Condition cond) {
    for (int i = 0; i < bucketsNr; ++i) {
        Node* current = hashTable[i];
        while (current) {
            for (int j = 0; j < current->size; ++j)
                if (!cond(current->values[j])) {
                    remove(current->key, current->values[j]);
                    j--;
                }
            current = current->next;
        }
    }
}

int MultiMap::get_bucketsNr() const {
    return bucketsNr;
}

void MultiMap::get_hashTable() const {
    for (int i = 0; i < bucketsNr; ++i) {
        Node* current = hashTable[i];
        while (current) {
            for (int j = 0; j < current->size; ++j) {
                std::cout << current->key << " " << current->values[j] << std::endl;
            }
            current = current->next;
        }
    }
}

