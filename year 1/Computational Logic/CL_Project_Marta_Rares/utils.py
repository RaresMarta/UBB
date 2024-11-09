# name: MARTA RARES-PETRU
# group: 1012
# specialisation: AI
# teacher: LUPEA MIHAELA

def read_option():
    """
    Reads an option from the user
    :return: int
    """
    try:
        option = int(input("Enter your option: "))
        if option < 0 or option > 9:
            raise ValueError
        return option

    except ValueError:
        print("Invalid option. Please enter a number between 0 and 9.")
        return read_option()


def read_nr(base):
    """
    Reads a number from the user
    :param base: int
    :return: str
    """
    digits = "0123456789ABCDEF"

    while len(digits) > base:
        digits = digits[:-1]

    try:
        a = input("Enter a number: ")
        if not a:
            raise ValueError("Empty input. Please enter a number.")
        if a[0] == "-":
            raise ValueError("Negative number. Please enter a positive integer.")
        if "," in a:
            raise ValueError("Invalid symbol(s). Use dot instead of comma")
        for i in range(len(a)):
            if (a[i] not in digits) and (a[i] != "."):
                raise ValueError(f"Invalid digit(s) in the number. Please enter a number in base {base}")
        return a

    except ValueError as e:
        print(e)
        return read_nr(base)


def read_base() -> int:
    """
    Reads the base from the user
    :return: int
    """
    try:
        base = int(input("Enter base: "))
        if base < 2 or base > 16:
            raise ValueError
        return base

    except ValueError:
        print("Invalid base. Please enter a number between 2 and 16.")
        return read_base()


def read_initial_base() -> int:
    """
    Reads the initial base from the user
    :return: int
    """
    try:
        base = int(input("Enter initial base: "))
        if base < 2 or base > 16:
            raise ValueError
        return base

    except ValueError:
        print("Invalid base. Please enter a number between 2 and 16.")
        return read_initial_base()


def read_final_base() -> int:
    """
    Reads the final base from the user
    :return: int
    """
    try:
        base = int(input("Enter final base: "))
        if base < 2 or base > 16:
            raise ValueError
        return base

    except ValueError:
        print("Invalid base. Please enter a number between 2 and 16.")
        return read_final_base()


def to_base_2(digit):
    """
    Converts a digit from base 10 to base 2
    :param digit:
    :return:
    """
    str_digits = "0123456789ABCDEF"
    digit = int(str_digits.index(digit))
    rez = ""

    while digit > 0:
        rez = str_digits[digit % 2] + rez
        digit = digit // 2

    return rez


def base_power(nr):
    """
    Calculates the power of 2 in a given number
    :param nr: int
    :return: int
    """
    k = 0
    while nr > 1:
        nr = nr // 2
        k += 1
    return k


def convert(a, base_a, base_b):
    """
    Converts a nr from base a to base b.
    It's basically the intermediate base method.
    :param a: string
    :param base_a: int
    :param base_b: int
    :return: string
    """
    digits = "0123456789ABCDEF"
    decimal = 0
    converted = ""

    for i in range(len(a)):
        digit = int(a[i], base_a)
        decimal += digit * (base_a ** (len(a) - i - 1))

    while decimal > 0:
        converted = digits[decimal % base_b] + converted
        decimal //= base_b

    if converted == "":
        converted = "0"

    return converted


def power(nr, p, base):
    """
    Calculates nr to the power p in a given base.
    :param nr: str
    :param p: int
    :param base: int
    :return: str
    """
    if p == 0:
        return "1"
    decimal_nr = convert(nr, base, 10)
    raised = int(decimal_nr) ** p
    raised_in_base = convert(str(raised), 10, base)
    return raised_in_base


def simplify(string):
    """
    Removes leading and trailing zeros from a string
    :param string: str
    :return: str
    """
    if "." in string:
        dot_index = string.index(".")
        i = 0
        while i < dot_index - 1 and string[0] == "0":
            string = string[1:]
            i += 1

        dot_index = string.index(".")
        i = len(string) - 1
        while i > dot_index + 1 and string[i] == "0":
            string = string[:len(string) - 1]
            dot_index = string.index(".")
            i -= 1

        if string[string.index(".") + 1:] == "0":
            string = string[:string.index(".")]

    else:
        while len(string) > 1 and string[0] == "0":
            string = string[1:]

    return string

