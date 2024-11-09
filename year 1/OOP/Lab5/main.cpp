#include <iostream>
#include "Animal.h"
#include "Mammal.h"
#include "Bird.h"
#include "Reptile.h"


int main() {
    Mammal whale("Whale", "Cetacea", true, 'A');
    Bird bird("Pigeon", "Columbidae", 10);
    Reptile rept("Viper", "Viperidae", true);
    whale.displayInfo();
    bird.displayInfo();
    rept.displayInfo();
    return 0;
}
