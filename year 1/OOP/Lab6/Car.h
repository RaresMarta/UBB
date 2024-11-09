#pragma once
#include <string>
#include <iostream>
#include "Vehicle.h"
using namespace std;


class Car: public Vehicle {
private:
    string bodyStyle;

public:
    Car(string reg, string bs);
    void display() override;
    string get_bodyStyle() const;
    void set_bodyStyle(string bs);
};
