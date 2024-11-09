#pragma once
#include <iostream>
#include "Duration.h"
#include <string>

using namespace std;


class Song {
private:
    string title, artist;
    static int characteristics[6];
    static Duration duration;


public:
    Song();
    Song(string t, string a, const int c[], const Duration& d);
    ~Song();

    int similarity(Song other);

    string get_title();
    string get_artist();
    static int get_characteristics();
    Duration get_duration();

    void set_title(string t);
    void set_artist(string a);
    void set_duration(Duration d);
    static void set_characteristics(const int c[]);
    static void set_to_zero();

};