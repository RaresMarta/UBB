#pragma once
#include <string>
using namespace std;

class Vehicle {
protected:
    string registrationNumber;

public:
    Vehicle(const string& reg) : registrationNumber(reg) {}
    virtual void display() = 0;
    virtual ~Vehicle() {};
};