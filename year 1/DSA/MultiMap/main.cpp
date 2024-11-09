#include <iostream>
#include "MultiMap.h"
#include "ExtendedTest.h"
#include "ShortTest.h"
#include "MultiMapIterator.h"

using namespace std;

// 28. ADT MultiMap – using a hashtable with separate chaining in which
// unique keys are stored with a dynamic array of the associated values

int main() {
    testAll();
    testAllExtended();
    cout << "End" << endl;
    system("pause");
    return 0;
}
