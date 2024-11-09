#include "ListIterator.h"
#include "IndexedList.h"
#include <exception>

ListIterator::ListIterator(const IndexedList& list) : list(list){
    current = list.head;
}

void ListIterator::first(){  /// O(1)
    if (list.isEmpty())
        current = -1;
    else
        current = list.head;
}

void ListIterator::next(){  /// O(1)
    if (!valid())
        throw std::exception();
    current = list.next[current];
}

bool ListIterator::valid() const{  /// O(1)
    return current != -1;
}

TElem ListIterator::getCurrent() const{  /// O(1)
    if (!valid())
        throw std::exception();
    return list.elems[current];
}