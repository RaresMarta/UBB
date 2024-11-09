#include "Reptile.h"


Reptile::Reptile(string c, string s, bool v): Animal(c, s) {
    isVenomous = v;
}

void Reptile::displayInfo() {
    cout << "[Reptile] " << endl;
    Animal::displayInfo();
    cout << "Is venomous: ";
    if (isVenomous)
        cout << "True" << endl;
    else
        cout << "False" << endl;
    cout << endl;
}