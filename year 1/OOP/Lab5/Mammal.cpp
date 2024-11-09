#include "Mammal.h"


Mammal::Mammal(string c, string s, bool a, unsigned char g): Animal(c, s) {
    isAquatic = a;
    gestationPeriod = g;
}

void Mammal::displayInfo() {
    cout << "[Mammal] " << endl;
    Animal::displayInfo();
    cout << "Is aquatic: ";
    if (isAquatic)
        cout << "True" << endl;
    else
        cout << "False" << endl;
    cout << "Gestation period: " << gestationPeriod << endl  << endl;
}