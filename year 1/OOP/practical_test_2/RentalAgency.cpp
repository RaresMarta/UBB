#include "RentalAgency.h"
#include <ostream>
#include <iostream>
#include <cstring>

std::ostream &operator<<(std::ostream& os, const RentalAgency &a) {
    for (int i = 0; i < a.get_inventory().size(); ++i) {
        os << *a.get_inventory()[i] << endl;
    }
    os << endl;
    return os;
}

vector<Vehicle*> RentalAgency::get_inventory() const {
    return inventory;
}

void RentalAgency::addVehicle(Vehicle* v) {
    inventory.push_back(v);
}

string RentalAgency::displayForRent(const string& vehicleType) const {
    for (int i = 0; i < inventory.size(); ++i) {
        if (typeid(inventory[i]).name() == vehicleType)
            std::cout << inventory[i] << " ";
        cout << endl << endl;
    }
}

RentalAgency::~RentalAgency() {
    for (Vehicle* v : inventory) {
        delete v;
    }
}

