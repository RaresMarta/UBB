#pragma once
#include "Animal.h"


class Bird: public Animal {
private:
    unsigned int wingSpan;

public:
    Bird(string c, string s, unsigned int w);
    void displayInfo();
};