#pragma once
#include <iostream>
#include <string>
using namespace std;


class Animal {
protected:
    string commonName;
    string scientificName;

public:
    void displayInfo();
    Animal(string c, string s): commonName(c), scientificName(s) {};
};