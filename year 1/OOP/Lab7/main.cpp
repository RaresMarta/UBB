#include <iostream>
#include <string>
using namespace std;


template<typename T>
void swapValue(T& a, T& b) {
    T aux = a;
    a = b;
    b = aux;
}


template<typename T>
T findMax(T a, T b) {
    return a > b ? a: b;
}



template<typename T1, typename T2>
class Pair {
private:
    T1 first;
    T2 second;

public:
    Pair(T1 a, T2 b): first(a), second(b) {}
    T1 get_first() { return first; }
    T2 get_second() { return second; }
    void set_first(T1 a) { first = a; }
    void set_second(T2 b) { second = b; }
};


void example() {
    cout << "swapValue - example" << endl;
    float a = 3.5, b = 7.9;
    cout << "a: " << a << " b: " << b << endl;
    swapValue(a, b);
    cout << "a: " << a << " b: " << b << endl << endl;

    int c = 10, d = 12;
    cout << "c: " << a << " d: " << b << endl;
    swapValue(a, b);
    cout << "c: " << a << " d: " << b << endl << endl;

    cout << "findMax - example" << endl;
    double e = 11111.55, f = 22222.6;
    cout << findMax(e, f) << endl;

    string g = "a", h = "b";
    cout << findMax(g, h) << endl << endl;

    cout << "Pair - example" << endl;
    Pair p1("Alex", 10);
    cout << p1.get_first() << ' ' << p1.get_second() << endl;
    Pair p2(190.2, 'A');
    cout << p2.get_first() << ' ' << p2.get_second() << endl << endl;
}

int main() {
    example();
    return 0;
}

