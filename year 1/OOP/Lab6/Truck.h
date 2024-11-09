#pragma once
#include <iostream>
#include <string>
#include "Vehicle.h"
using namespace std;


class Truck: public Vehicle {
private:
    double payloadCapacity;

public:
    Truck(string reg, double pc);
    void display() override;
    double get_payloadCap() const;
    void set_payloadCap(double pc);
};
