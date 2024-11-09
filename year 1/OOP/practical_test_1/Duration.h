#pragma once
#include <iostream>
using namespace std;


class Duration {
private:
    int min, sec;

public:
    Duration();
    Duration(int minutes, int seconds);
    ~Duration();

    int get_min();
    int get_sec();
    void set_min(int new_min);
    void set_sec(int new_sec);

    static int durationDifference(const Duration& d1, const Duration& d2);
};