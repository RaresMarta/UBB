#include "ShortTest.h"
#include "MultiMap.h"
#include "MultiMapIterator.h"
#include <assert.h>
#include <vector>
#include<iostream>

bool filter_function(TValue v) {
    if (v % 2 != 0)
        return true;
    else return false;
}

void testAll() {
    MultiMap m;
    m.add(1, 100);
    m.add(2, 200);
    m.add(3, 300);
    m.add(1, 500);
    m.add(2, 600);
    m.add(4, 800);

    assert(m.size() == 6);

    assert(m.remove(5, 600) == false);
    assert(m.remove(1, 500) == true);

    assert(m.size() == 5);

    vector<TValue> v;
    v=m.search(6);
    assert(v.size()==0);

    v=m.search(1);
    assert(v.size()==1);

    assert(m.isEmpty() == false);

    MultiMapIterator im = m.iterator();
    assert(im.valid() == true);
    while (im.valid()) {
        im.getCurrent();
        im.next();
    }
    assert(im.valid() == false);
    im.first();
    assert(im.valid() == true);

    // Test filter
    MultiMap mlt;
    mlt.add(1, 100);
    mlt.add(2, 200);
    mlt.add(3, 300);
    mlt.add(1, 500);
    mlt.add(2, 600);
    mlt.add(4, 800);

    mlt.filter(filter_function);

    if (!mlt.isEmpty()) {
        MultiMapIterator imm = mlt.iterator();
        while (imm.valid()) {
            TElem current = imm.getCurrent();
            cout << current.first << " " << current.second << endl;
            imm.next();
        }
    }

    assert(mlt.isEmpty() == true);

}
