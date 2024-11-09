#include "Vehicle.h"
#include <sstream>
#include <stdexcept>

Vehicle::Vehicle(const Vehicle &v) {
    this->model = v.get_model();
    this->year = v.get_year();
    this->dailyRate = v.get_dailyRate();
}

Vehicle::Vehicle(const std::string &m, int y, double dr) {
    model = m;
    year = y;
    if (dr < 10)
        throw invalid_argument{"Invalid daily rate!"};
    else
        dailyRate = dr;
}

string Vehicle::get_model() const { return this->model; }
int Vehicle::get_year() const { return this->year; }
double Vehicle::get_dailyRate() const { return this->dailyRate;}

void Vehicle::set_model(const string& m) {
    this->model = m;
}

void Vehicle::set_year(int y) {
    this->year = y;
}

void Vehicle::set_dailyRate(double dr) {
    if(dr < 10)
        throw invalid_argument{"Invalid daily rate!"};
    else this->dailyRate = dr;
}

ostream &operator<<(ostream &os, const Vehicle& v) {
    os << v.display();
    return os;
}

