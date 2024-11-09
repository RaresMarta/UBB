#include "Bike.h"
#include <sstream>


Bike::Bike(const Bike &b): Vehicle(b) {
    this->bikeType = b.get_bikeType();
}

string Bike::get_bikeType() const { return this->bikeType; }

void Bike::set_bikeType(string bt) {
    this->bikeType = bt;
}

string Bike::display() const {
    ostringstream oss;
    oss << "[BIKE]" << "\n";
    oss << "Model: " << this->get_model() << "\n";
    oss << "Year: " << this->get_year() << "\n";
    oss << "Daily Rate: " << this->get_dailyRate() << "\n";
    oss << "Bike type: " << this->get_bikeType() << "\n";
    return oss.str();
}

