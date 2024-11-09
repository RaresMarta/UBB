#include "Car.h"
#include <iostream>
using namespace std;


Car::Car(string reg, string bs): Vehicle(reg){
    bodyStyle = bs;
}

void Car::display() {
    cout << "[Car]" << endl;
    cout << "Registration nr: " << registrationNumber << endl;
    cout << "Body style: " << bodyStyle << endl;
}

string Car::get_bodyStyle() const {
    return bodyStyle;
}

void Car::set_bodyStyle(string bs) {
    bodyStyle = bs;
}