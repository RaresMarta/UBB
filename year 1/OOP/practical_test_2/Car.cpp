#include "Car.h"
#include <sstream>
#include <algorithm>
#include <stdexcept>


vector<string> fuels = {"Diesel", "diesel", "Gas", "gas", "Gasoline", "gas", "Electric", "electric"};
bool fuel_valid(const string& fuel) {
    return find(fuels.begin(), fuels.end(), fuel) != fuels.end();
}

// copy constructor
Car::Car(const Car &c): Vehicle(c) {
    this->seats = c.get_seats();
    if (!fuel_valid(c.get_fuelType()))
        throw invalid_argument{"Invalid fuel type!"};
    else
        this->fuelType = c.get_fuelType();
}

// getters
int Car::get_seats() const { return this->seats; }
string Car::get_fuelType() const { return this->fuelType; }

// setters
void Car::set_seats(int s) {
    this->seats = s;
}

void Car::set_fuelType(const string &ft) {
    if (!fuel_valid(ft))
        throw invalid_argument{"Invalid fuel type!"};
    this->fuelType = ft;
}

string Car::display() const {
    ostringstream oss;
    oss << "[CAR]" << "\n";
    oss << "Model: " << this->get_model() << "\n";
    oss << "Year: " << this->get_year() << "\n";
    oss << "Daily Rate: " << this->get_dailyRate() << "\n";
    oss << "Seats number: " << this->get_seats() << "\n";
    oss << "Fuel type: " << this->get_fuelType() << "\n";
    return oss.str();
}


