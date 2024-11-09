#pragma once
#include "Song.h"
#include <iostream>
#include <string>
#include <cmath>
using namespace std;


bool unique(int nr, const int arr[]) {
    for (int i = 0; i <= 5; i++)
        if (nr == arr[i])
            return false;
    return true;
}

Song::Song() {
    int x = 1 + rand() % 10;
    int z = 3 + rand() % 7;
    this->title = "Title " + to_string(x);
    this->artist = "Artist " + to_string(z);
    this->duration.set_min(3);
    this->duration.set_sec(1 + rand() % 60);
    for (int i = 0; i <= 5; i++) {
        int random = 1 + rand() % 100;
        if (unique(random, reinterpret_cast<const int *>(characteristics)))
            this->characteristics[0] = random;

    }
}

Song::Song(std::string t, std::string a, const int c[], const Duration& d) {
    this->title = t;
    this->artist = a;
    for (int i = 0; i <= 5; i++)
        this->characteristics[i] = c[i];
    this->duration = d;

}

Song::~Song() = default;

string Song::get_title() { return this->title; }
string Song::get_artist() {return this->artist; }
//int Song::get_characteristics() { return characteristics[]; }
Duration Song::get_duration() {return this->duration; }

void Song::set_title(string t) { this->title = t; }
void Song::set_artist(string a) { this->artist = a; }
void Song::set_duration(Duration d) { this->duration = d; }

void Song::set_characteristics(const int *c) {
    if (c[0] == 0)
        for (int i = 1; i <= 5; i++) {
            if (c[i] != 0) {
                cout << "Invalid characteristics" << endl;
                break;
            }
        }
    else {
        for (int i = 0; i <= 5; i++)
            if (c[i] >= 1 && c[i] <= 100)
                characteristics[i] = c[i];
            else {
                cout << "Invalid characteristics" << endl;
                break;
            }
    }
}

void Song::set_to_zero() {
    for (int i = 0; i <= 5; i++)
        characteristics[i] = 0;
}

int Song::similarity(Song other) {
    if (duration.durationDifference(this->duration, other.get_duration()) <= 30) {
        int sum1 = 0;
        for (int i = 0; i <= 5; i++)
            sum1 += this->characteristics[i] * other.characteristics[i];

        int sum2 = 0;
        int sum3 = 0;
        for (int i = 0; i <= 5; i++) {
            sum1 += this->characteristics[i] * this->characteristics[i];
            sum2 += other.characteristics[i] * other.characteristics[i];
        }
        int cosine_similarity = sum1 / (sqrt(sum2) * sqrt(sum3));
        return 1 - cosine_similarity;
    }
    return -1;
}
