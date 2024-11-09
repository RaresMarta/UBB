#include <iostream>
#include "Garage.h"
#include "Car.h"
#include "Truck.h"


int main() {
    Garage g;
    Car* car1;
    Truck* truck1;

    car1 = new Car("1", "Sedan");
    truck1 = new Truck("2", 1000);

    g.addVehicle(car1);
    g.addVehicle(truck1);

    g.display();

    return 0;
}
