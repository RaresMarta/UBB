#pragma once
#include "Character.h"
#include <vector>
#include <algorithm>
using namespace std;


class Wizard: public Character {
private:
    int mana, spellPower;
    vector<string> spells;

public:
    Wizard(string &n, int &h, int &l, int &m, vector<string> &sp, int &spwr);
    bool castSpell(const string& spell);
};