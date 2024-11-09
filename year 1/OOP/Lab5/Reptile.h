#pragma once
#include "Animal.h"


class Reptile: public Animal {
private:
    bool isVenomous;

public:
    Reptile(string c, string s, bool v);
    void displayInfo();
};