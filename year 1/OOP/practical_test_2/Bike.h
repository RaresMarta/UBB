#pragma once
#include "Vehicle.h"

class Bike: public Vehicle {
private:
    string bikeType;

public:
    Bike(const string& m, int y, double dr, const string& bt):
            Vehicle(m, y, dr), bikeType(bt) {};
    Bike(const Bike& b);
    ~Bike() = default;

    string display() const override;

    string get_bikeType() const;
    void set_bikeType(string bt);
};