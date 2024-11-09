#include "Wizard.h"


Wizard::Wizard(string &n, int &h, int &l, int &m, vector<string> &sp, int &spwr)
        : Character(n, h, l) {
    mana = m;
    spells = sp;
    spellPower = spwr;
}

bool Wizard::castSpell(const string& spell) {
    if (find(spells.begin(), spells.end(), spell) != spells.end() || mana < 10)
        return false;
    mana -= 10;
    return true;
}
