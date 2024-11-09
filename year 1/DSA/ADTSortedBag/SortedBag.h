#pragma once
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);
#define NULL_TCOMP -11111;

class SortedBagIterator;

class SortedBag {
    friend class SortedBagIterator;
    struct Pair {
        TComp elem;
        int freq;
    };

private:
    int capacity;
    int nrPairs;
    Pair* data;
    Relation rel;
    void resize();

public:
    //constructor
    explicit SortedBag(Relation r);

    //destructor
    ~SortedBag();

    //adds an elem to the sorted bag
    void add(TComp e);

    //removes one occurrence of an elem from a sorted bag
    //returns true if an elem was removed, false otherwise (if e was not part of the sorted bag)
    bool remove(TComp e);

    //checks if an elem appears is the sorted bag
    bool search(TComp e) const;

    int elemIndex(TComp e) const;

    //returns the number of occurrences for an elem in the sorted bag
    int nrOccurrences(TComp e) const;

    //returns the number of elements from the sorted bag
    int get_size() const;

    //returns an iterator for this sorted bag
    SortedBagIterator iterator() const;

    //checks if the sorted bag is empty
    bool isEmpty() const;

};