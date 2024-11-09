from Repository import *


def read_file(file_name):
    """
    Reads a file.
    :param file_name: str
    :return: list
    """
    with open(file_name, "r") as file:
        data = file.readlines()
        data = [x.strip().split(",") for x in data]
        return data


def main_menu():
    """Main menu function."""
    data = read_file("InputFile")
    print(data)
    repo = Repository()
    for line in data:
        repo.add_item(int(line[0]), line[1], line[2], int(line[3]), int(line[4]))
    opt = 1
    while opt != 0:
        opt = int(input("1 - Add a new workout routine.\n"
                        "2 - Sort workout routines.\n"
                        "3 - Remove workout routines.\n"
                        "4 - Display all workout routines.\n"
                        "0 - Exit.\n"
                        "Option: "))
        if opt == 1:
            Id = int(input("Id: "))
            name = input("Name: ")
            typ = input("Type: ")
            dif = int(input("Difficulty: "))
            dur = int(input("Duration: "))
            repo.add_item(Id, name, typ, dif, dur)
        elif opt == 2:
            repo.sort_workouts()
        elif opt == 3:
            repo.remove_workouts()
        elif opt == 4:
            print(repo.get_all())
        elif opt == 0:
            print("End of program.")


if __name__ == '__main__':
    main_menu()
