from ui.ui import *
import unittest
from tests.test_Project import *
from tests.test_ProjectRepo import *

if __name__ == "__main__":
    print("Do you wish to run tests or the program?")
    print("1. Run tests")
    print("2. Run program")
    print("0. Exit")
    while True:
        option = int(input("Please enter an option: "))
        if option == 1:
            unittest.main(exit=False)
        elif option == 2:
            main_menu()
        elif option == 0:
            print("Thank you for using the project manager!")
            break
        else:
            print("Invalid option")
