#include "Duration.h"
#pragma once
#include <iostream>
using namespace std;


Duration::Duration() {
    this->min = 3;
    this->sec = 0;
}

Duration::Duration(int minutes, int seconds) {
    this->min = minutes;
    this->sec = seconds;
}

Duration::~Duration() = default;

int Duration::get_min() { return this->min; }
int Duration::get_sec() { return this->sec; }

void Duration::set_min(int new_min) {
    if (new_min >= 1 && new_min <= 10)
        this->min = new_min;
    else
        cout << "Invalid minutes, setter failed";
}

void Duration::set_sec(int new_sec) {
    if (new_sec >= 1 && new_sec <= 60)
        this->sec = new_sec;
    else
        cout << "Invalid seconds, setter failed";
}

int Duration::durationDifference(const Duration& d1, const Duration& d2) {
    int s1 = d1.min * 60 + d1.sec;
    int s2 = d2.min * 60 + d2.sec;
    return abs(s1 - s2);
}