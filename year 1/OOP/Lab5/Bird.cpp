#include "Bird.h"


Bird::Bird(string c, string s, unsigned int w): Animal(c, s) {
    wingSpan = w;
}

void Bird::displayInfo() {
    cout << "[Bird]" << endl;
    Animal::displayInfo();
    cout << "Wing span: " << wingSpan << endl << endl;
}