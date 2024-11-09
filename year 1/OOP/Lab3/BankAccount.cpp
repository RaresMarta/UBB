#include <iostream>
#include "BankAccount.h"
using namespace std;

BankAccount::BankAccount(string name, double number, double init_balance) {
    holder_name = name;
    account_number = number;
    account_balance = init_balance;
}

BankAccount::~BankAccount() = default;

string BankAccount::get_name() {
    return holder_name;
}

double BankAccount::get_number() {
    return account_number;
}

double BankAccount::get_balance() {
    return account_balance;
}

void BankAccount::deposit(double amount) {
    account_balance += amount;
    cout << "Deposited: " << amount << endl;
}

void BankAccount::withdraw(double amount) {
    if(account_balance >= amount) {
        account_balance -= amount;
        cout << "Withdrawn: " << amount << endl;
    }
    else {
        cout << "Insufficient funds" << endl;
    }
}

ostream& operator<<(ostream& os, const BankAccount& acc) {
    os << "(name: " << acc.holder_name << ", number: " << acc.account_number << ", balance: " << acc.account_balance << ")" << endl;
    return os;
}
