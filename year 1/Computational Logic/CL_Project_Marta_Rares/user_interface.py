from main import *
from utils import *


print("MARTA RARES-PETRU - 1012 - AI - LUPEA MIHAELA")
print("1. Addition of two numbers in a given base")
print("2. Subtraction of two numbers in a given base")
print("3. Multiplication of two numbers in a given base")
print("4. Division of two numbers in a given base")
print("5. Rapid conversion from base p = 2 ^ k into base 2; p = {4, 8, 16}")
print("6. Rapid conversion from base 2 into base q = 2 ^ k; q = {4, 8, 16}")
print("7. Conversion using the substitution method")
print("8. Conversion using the successive divisions/multiplications method")
print("9. Conversion by using an intermediate base")
print("0. Exit")

option = read_option()

while 1 <= option <= 9:
    if option == 1:
        base = read_base()
        a = read_nr(base)
        b = read_nr(base)
        print("Result:", addition(a, b, base))

    elif option == 2:
        base = read_base()
        a = read_nr(base)
        b = read_nr(base)
        print("Result:", subtraction(a, b, base))

    elif option == 3:
        base = read_base()
        a = read_nr(base)
        b = read_nr(base)
        while len(a) != 1 and len(b) != 1:
            print("Multiplication is possible only by one digit, please try again")
            a = read_nr(base)
            b = read_nr(base)
        print("Result:", multiplication(a, b, base))

    elif option == 4:
        base = read_base()
        a = read_nr(base)
        b = read_nr(base)
        while len(a) != 1 and len(b) != 1:
            print("Division is possible only by one digit, please try again")
            a = read_nr(base)
            b = read_nr(base)
        result = division(a, b, base)
        print(f"Result: {result[0]} remainder {result[1]}")

    elif option == 5:
        base = read_base()  # base p = 2^k
        a = read_nr(base)
        print("Result:", base_p_to_base_2(a, base))

    elif option == 6:
        base = read_base()  # base q = 2^k
        a = read_nr(base)
        print("Result:", base_2_to_base_q(a, base))

    elif option == 7:
        from_base = read_initial_base()
        a = read_nr(from_base)
        to_base = read_final_base()
        print("Result:", substitution_method(a, from_base, to_base))

    elif option == 8:
        from_base = read_initial_base()
        a = read_nr(from_base)
        to_base = read_final_base()
        print("Result:", successive_div_and_mult(a, from_base, to_base))

    elif option == 9:
        from_base = read_initial_base()
        a = read_nr(from_base)
        to_base = read_final_base()
        print("Result:", intermediate_base(a, from_base, to_base))

    option = read_option()


exit()
