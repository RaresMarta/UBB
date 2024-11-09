#pragma once

#include <vector>
#include "Vehicle.h"


class Car: public Vehicle {
private:
    int seats;
    string fuelType;

public:
    Car(const string& m, int y, double dr, int s, const string& ft):
            Vehicle(m, y, dr), seats(s), fuelType(ft) {};
    Car(const Car& c);
    ~Car() = default;

    string display() const override;

    int get_seats() const;
    string get_fuelType() const;

    void set_seats(int s);
    void set_fuelType(const string& ft);
};