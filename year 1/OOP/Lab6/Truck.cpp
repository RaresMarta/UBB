#include "Truck.h"


Truck::Truck(string reg, double pc): Vehicle(reg) {
    payloadCapacity = pc;
}

void Truck::display() {
    cout << "[Truck]" << endl;
    cout << "Registration nr: " << registrationNumber << endl;
    cout << "Payload Capacity: " << payloadCapacity << endl;
}

double Truck::get_payloadCap() const {
    return payloadCapacity;
}

void Truck::set_payloadCap(double pc) {
    payloadCapacity = pc;
}


