#pragma once
#include "Character.h"
#include <iostream>
using namespace std;


class Knight: public Character {
private:
    float armor;
    int swordDamage;

public:
    Knight(string &n, int &h, int &l, float &a, int &dmg) : Character(n, h, l), armor(a), swordDamage(dmg) {};
    void takeDamage(int damage);
};