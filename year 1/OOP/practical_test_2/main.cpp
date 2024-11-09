#include "Car.h"
#include "Bike.h"
#include "RentalAgency.h"
#include <iostream>
#include <stdexcept>
using namespace std;


int main() {
    try {
        RentalAgency a;
        Car* c1 = new Car("bmw", 2005, 15, 5, "Diesel");
        Car* c2 = new Car("Audi", 2019, 16, 2, "Gasoline");
        Bike* b1 = new Bike("Yamaha", 2020, 12, "Mountain");

        a.addVehicle(c1);
        a.addVehicle(c2);
        a.addVehicle(b1);

        cout << a;
    }
    catch (invalid_argument& e) {
        cerr << e.what() << "\n";
    }
    return 0;
}
