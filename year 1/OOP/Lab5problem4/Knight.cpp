//
// Created by ROG on 4/19/2024.
//

#include "Knight.h"

void Knight::takeDamage(int damage) {
    this->armor -= damage;
    if (this->armor < 0)
        this->health = 0;
}
