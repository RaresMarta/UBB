# main.py
# name: MARTA RARES-PETRU
# group: 1012
# specialisation: AI
# teacher: LUPEA MIHAELA

from utils import convert, power, simplify, base_power


def addition(a: str, b: str, base: int) -> str:
    """
    Adds two numbers represented as strings in a given base.
    :param a: str
    :param b: str
    :param base: int
    :return: str
    """
    # Convert to base 10
    a_decimal = int(convert(a, base, 10))
    b_decimal = int(convert(b, base, 10))

    # Perform addition
    result_decimal = a_decimal + b_decimal

    # Convert result back to original base
    return convert(str(result_decimal), 10, base)


def subtraction(a: str, b: str, base: int) -> str:
    """
    Subtracts two numbers represented as strings in a given base.
    :param a: str
    :param b: str
    :param base: int
    :return: str
    """
    a_decimal = int(convert(a, base, 10))
    b_decimal = int(convert(b, base, 10))

    # Perform subtraction
    result_decimal = a_decimal - b_decimal

    # Ensure result is non-negative and convert back to original base
    if result_decimal < 0:
        raise ValueError("Result is negative. Subtraction not supported for negative values.")

    return convert(str(result_decimal), 10, base)


def multiplication(a: str, b: str, base: int) -> str:
    """
    Multiplies two numbers represented as strings in a given base.
    :param a: str
    :param b: str
    :param base: int
    :return: str
    """
    a_decimal = int(convert(a, base, 10))
    b_decimal = int(convert(b, base, 10))

    # Perform multiplication
    result_decimal = a_decimal * b_decimal

    return convert(str(result_decimal), 10, base)


def division(a: str, b: str, base: int) -> tuple:
    """
    Divides two numbers represented as strings in a given base.
    Returns the quotient and remainder.
    :param a: str
    :param b: str
    :param base: int
    :return: tuple (quotient, remainder)
    """
    a_decimal = int(convert(a, base, 10))
    b_decimal = int(convert(b, base, 10))

    if b_decimal == 0:
        raise ValueError("Division by zero is not allowed.")

    # Perform division
    quotient = a_decimal // b_decimal
    remainder = a_decimal % b_decimal

    # Convert results back to original base
    return (convert(str(quotient), 10, base), convert(str(remainder), 10, base))


def base_p_to_base_2(a: str, base_p: int) -> str:
    """
    Converts a number from base p (p = 2^k) to base 2.
    Pads the output with leading zeros to maintain consistent length.
    :param a: str - The input number in base p
    :param base_p: int - The source base (must be a power of 2)
    :return: str - The converted number in base 2, with leading zeros preserved
    """
    result = convert(a, base_p, 2)

    # Calculate expected length based on the power of base_p (e.g., base 16 -> 4 bits per digit)
    power_of_2 = base_power(base_p)  # gives how many bits are used per digit in base_p
    expected_length = len(a) * power_of_2  # Total expected bit length for the base 2 representation

    # Pad with leading zeros to reach the expected length
    return result.zfill(expected_length)


def base_2_to_base_q(a: str, base_q: int) -> str:
    """
    Converts a number from base 2 to base q (q = 2^k).
    :param a: str
    :param base_q: int
    :return: str
    """
    return convert(a, 2, base_q)


def substitution_method(a: str, from_base: int, to_base: int) -> str:
    """
    Converts a number from `from_base` to `to_base` using the substitution method.
    :param a: str - The input number in `from_base`
    :param from_base: int - The source base
    :param to_base: int - The target base
    :return: str - The converted number in `to_base`
    """
    # Step 1: Convert `a` from `from_base` to decimal
    digits = "0123456789ABCDEF"
    decimal_value = 0
    a = a.upper()  # Handle uppercase letters for bases > 10

    for i, digit in enumerate(reversed(a)):
        value = digits.index(digit)
        decimal_value += value * (from_base ** i)

    # Step 2: Convert `decimal_value` to `to_base`
    if decimal_value == 0:
        return "0"

    result = ""
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = digits[remainder] + result
        decimal_value //= to_base

    return result


def successive_div_and_mult(a: str, from_base: int, to_base: int) -> str:
    """
    Converts a number from `from_base` to `to_base` using successive division.
    :param a: str - The input number in `from_base`
    :param from_base: int - The source base
    :param to_base: int - The target base
    :return: str - The converted number in `to_base`
    """
    # Step 1: Convert `a` from `from_base` to decimal
    digits = "0123456789ABCDEF"
    decimal_value = 0
    a = a.upper()

    for i, digit in enumerate(reversed(a)):
        value = digits.index(digit)
        decimal_value += value * (from_base ** i)

    # Step 2: Convert `decimal_value` to `to_base` using successive division
    if decimal_value == 0:
        return "0"

    result = ""
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = digits[remainder] + result
        decimal_value //= to_base

    return result


def intermediate_base(a: str, from_base: int, to_base: int) -> str:
    """
    Converts a number from `from_base` to `to_base` using an intermediate base (decimal).
    :param a: str - The input number in `from_base`
    :param from_base: int - The source base
    :param to_base: int - The target base
    :return: str - The converted number in `to_base`
    """
    # Step 1: Convert `a` from `from_base` to decimal
    digits = "0123456789ABCDEF"
    decimal_value = 0
    a = a.upper()

    for i, digit in enumerate(reversed(a)):
        value = digits.index(digit)
        decimal_value += value * (from_base ** i)

    # Step 2: Convert `decimal_value` to `to_base`
    if decimal_value == 0:
        return "0"

    result = ""
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result = digits[remainder] + result
        decimal_value //= to_base

    return result


