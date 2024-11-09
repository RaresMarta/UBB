#pragma once
#include "Vehicle.h"
#include <vector>
#include <ostream>

class RentalAgency {
private:
    vector<Vehicle*> inventory;

public:
    ~RentalAgency();
    vector<Vehicle*> get_inventory() const;
    string displayForRent(const string& vehicleType) const;
    void addVehicle(Vehicle* v);
    friend std::ostream &operator<<(std::ostream& os, const RentalAgency& a);
};