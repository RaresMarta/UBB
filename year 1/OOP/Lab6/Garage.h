#pragma once
#include <vector>
#include "Vehicle.h"
#include <iostream>
using namespace std;


class Garage {
private:
    vector<Vehicle*> vehicles;

public:
    void display();
    void addVehicle(Vehicle *v);
    ~Garage();
};