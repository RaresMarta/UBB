#pragma once
#include <string>
#include <ostream>
using namespace std;


class Vehicle {
protected:
    string model;
    int year;
    double dailyRate;

public:
    Vehicle(const string& m, int y, double dr);
    Vehicle(const Vehicle& v);
    virtual ~Vehicle() = default;
    string get_model() const;
    int get_year() const;
    double get_dailyRate() const;

    void set_model(const string& m);
    void set_year(int y);
    void set_dailyRate(double dr);

    virtual string display() const = 0;

    friend ostream& operator<<(ostream& os, const Vehicle& v);
};