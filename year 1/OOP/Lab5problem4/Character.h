#pragma once
#include <string>
using namespace std;


class Character {
protected:
    string name;
    int health, level;

public:
    Character(string &n, int &h, int &l): name(n), health(h), level(l) {};

    string get_name() const;
    int get_health() const;
    int get_level() const;

    void set_name(string &newName);
    void set_health(int &newHealth);
    void set_level(int &newLevel);
};