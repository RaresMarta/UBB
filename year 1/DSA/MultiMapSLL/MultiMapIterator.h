
#pragma once
#include "MultiMap.h"

class MultiMap;

class MultiMapIterator
{
	friend class MultiMap;

private:
	const MultiMap& col;
    MultiMap::Node* current;
    int index, position;
    int bucketsNr;
	MultiMapIterator(const MultiMap& c);

public:
	TElem getCurrent() const;
	bool valid() const;
	void next();
	void first();
};



/*
#pragma once
#include "MultiMap.h"

class MultiMap;

class MultiMapIterator
{
    friend class MultiMap;

private:
    const MultiMap& col;
    //TODO - Representation
    MultiMap::Node* currentElem;
    int currentindex;
    int currentpos;
    void move();
    //DO NOT CHANGE THIS PART
    MultiMapIterator(const MultiMap& c);

public:
    TElem getCurrent()const;
    bool valid() const;
    void next();
    void first();
};

*/