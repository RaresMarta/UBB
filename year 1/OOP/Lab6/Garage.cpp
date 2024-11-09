#include "Garage.h"


void Garage::display() {
    for (int i = 0; i < vehicles.size(); i++) {
        vehicles[i]->display();
    }
    cout << endl;
}

void Garage::addVehicle(Vehicle *v) {
    vehicles.push_back(v);
}

Garage::~Garage() {
    for (int i = 0; i < vehicles.size(); i++) {
        delete vehicles[i];
    }
}
