#include <iostream>
#include "Song.h"
using namespace std;

int main() {
    int chr[6] = {10,20,30,40,50,60};
    Song s1("title1", "artist1", chr, Duration(2,10));

    int chr2[6] = {20, 50, 40, 30, 10, 70};
    Song *s2 = new Song("title2", "artist2", chr2, Duration(3,10));

    Song songs[100];
    songs[0] = s1;
    songs[1] = *s2;
    for (int i = 2; i <= 99; i++)
        songs[i] = Song();

    Song toMatch;
    int arr[6] = {19, 13, 2, 76, 82};
    toMatch.set_characteristics(arr);
    toMatch.set_duration(Duration(2,45));

    int maximum = 0;
    Song the_song;
    for (int i = 0; i < 100; i++) {
        int sim = songs[i].similarity(toMatch);
        if (sim > maximum){
            maximum = sim;
            the_song = songs[i];
        }
    }

    return 0;
}

