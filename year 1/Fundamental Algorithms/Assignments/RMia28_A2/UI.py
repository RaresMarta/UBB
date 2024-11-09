import functions
from functions import read
from functions import list_input

if __name__ == "__main__":
    print("Numeric arrays")
    print("Choose one of the following features:")
    print("0. Stop")
    print("1. Add a value to the end of the list")
    print("2. Insert a value at a specified index")
    print("3. Remove a value at a specified index")
    print("4. Remove elements between two given indexes")
    print("5. Replace all old values occurances with new value")
    print("6. Print the prime numbers between two given indexes")
    print("7. Print the odd numbers between two given indexes")
    print("8. Sum the elements between two given indexes")
    print("9. Get the GCD of elements between two given indexes")
    print("10. Get the maximum of elements between two given indexes")
    print("11. Remove elements from the list that are not prime")
    print("12. Remove elements from the list that are positive")
    print("13. Undo the last operation that modified the array")
    past_lists = []
    current_list = []
    last_option = 0
    print("Choose a feature: ")
    option = read()
    while option != 0:
        if option == 1:
            print("Add a number to the end of the list:")
            nr = read()
            functions.add(current_list, nr)
            past_lists.append(current_list[:])
            print("Current list:",current_list)
        elif option == 2:
            print("- insert number: ")
            nr = read()
            print("- at index:")
            index = read()
            functions.insert(current_list, nr, index)
            past_lists.append(current_list[:])
            print("Current list:", current_list)
        elif option == 3:
            print("- deleting value at index:")
            index = read()
            functions.remove(current_list, index)
            past_lists.append(current_list[:])
            print("Current list:", current_list)
        elif option == 4:
            print("- enter first index")
            from_index = read()
            print("- enter second index")
            to_index = read()
            functions.remove_sequence(current_list, from_index, to_index)
            past_lists.append(current_list[:])
            print("Current list:", current_list)
        elif option == 5:
            print("- cardinal of the old sequence:")
            crt1 = read()
            print("- elements")
            old = list_input(crt1)
            print("- cardinal of the new sequence:")
            crt2 = read()
            print("- elements")
            new = list_input(crt2)
            functions.replace(current_list, old, new)
            past_lists.append(current_list[:])
            print("Current list:", current_list)
        elif option == 6:
            print("- enter first index")
            from_index = read()
            print("- enter second index")
            to_index = read()
            print(functions.prime(current_list, from_index, to_index))
        elif option == 7:
            print("- enter first index")
            from_index = read()
            print("- enter second index")
            to_index = read()
            print(functions.odd(current_list, from_index, to_index))
        elif option == 8:
            print("- enter first index")
            from_index = read()
            print("- enter second index")
            to_index = read()
            print(functions.suma(current_list, from_index, to_index))
        elif option == 9:
            print("- enter first index")
            from_index = read()
            print("- enter second index")
            to_index = read()
            print(functions.gcd(current_list, from_index, to_index))
        elif option == 10:
            print("- enter first index")
            from_index = read()
            print("- enter second index")
            to_index = read()
            print(functions.max(current_list, from_index, to_index))
        elif option == 11:
            print("Removing non-prime numbers...")
            functions.filter_prime(current_list)
            past_lists.append(current_list[:])
            print("Current list:", current_list)
        elif option == 12:
            print("Removing positive numbers...")
            functions.filter_negative(current_list)
            past_lists.append(current_list[:])
            print("Current list:", current_list)
        elif option == 13:
            functions.undo(past_lists, last_option)
            current_list = past_lists[len(past_lists)-1].copy()
            print("Last operation undone!")
            print("Current list:", current_list)
        last_option = option
        print("Choose a feature: ")
        option = read()

