#pragma once
#include <ostream>
#include <istream>
using namespace std;

class BankAccount {
    private:
        string holder_name;
        double account_number;
        double account_balance;

    public:
        // parameterized constructor declaration
        BankAccount(string name, double number, double balance);
        ~BankAccount(); // destructor

        string get_name();
        double get_number();
        double get_balance();

        void deposit(double amount);
        void withdraw(double amount);

        friend ostream& operator<<(ostream& os, const BankAccount& acc);
};