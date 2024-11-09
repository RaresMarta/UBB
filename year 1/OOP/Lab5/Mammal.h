#pragma once
#include "Animal.h"

class Mammal: public Animal {
private:
    bool isAquatic;
    unsigned char gestationPeriod;

public:
    Mammal(string c, string s, bool a, unsigned char g);
    void displayInfo();
};