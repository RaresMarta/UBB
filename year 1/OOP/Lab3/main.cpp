#include "BankAccount.h"
#include <iostream>
using namespace std;

int main() {
    BankAccount a1("Alex", 10, 2000);

    cout << a1;

    a1.deposit(500);
    cout << "Updated balance: " << a1.get_balance() << endl << endl;

    a1.withdraw(2600);
    cout << "Updated balance: " << a1.get_balance() << endl << endl;

    a1.withdraw(100);
    cout << "Updated balance: " << a1.get_balance() << endl << endl;

    return 0;
}