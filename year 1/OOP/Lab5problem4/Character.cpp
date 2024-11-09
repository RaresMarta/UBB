#include "Character.h"


string Character::get_name() const { return name; }
int Character::get_health() const { return health; }
int Character::get_level() const { return level; }

void Character::set_name(string &newName) { name = newName; }
void Character::set_health(int &newHealth) { health = newHealth; }
void Character::set_level(int &newLevel) { level = newLevel; }