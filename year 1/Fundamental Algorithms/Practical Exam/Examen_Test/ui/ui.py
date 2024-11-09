from src.Project import Project
from repo.ProjectRepo import ProjectRepo


def read_from_file(file):
    with open(file, "r") as f:
        lines = f.readlines()
        return [line.strip("\n") for line in lines]


def main_menu():
    repo = ProjectRepo()
    projects = read_from_file("InputData")
    for project in projects:
        project = project.split(",")
        repo.add_project(Project(project[0], project[1], project[2], int(project[3])))
    print("Welcome to the project manager!")
    print("1. Add a project")
    print("2. Delete a project")
    print("3. Update the number of participants by theme")
    print("4. Print all projects")
    print("0. Exit")
    print("The current projects are: \n" + str(repo))
    while True:
        try:
            option = int(input("Please enter an option: "))
            if option == 1:
                name = input("Please enter the name of the project: ")
                theme = input("Please enter the theme of the project: ")
                rep_name = input("Please enter the representative name of the project: ")
                number = int(input("Please enter the number of participants of the project: "))
                repo.add_project(Project(name, theme, rep_name, number))
                print(repo)
            elif option == 2:
                rep_name = input("Please enter the name of the project: ")
                repo.delete_by_name(rep_name)
                print(repo)
            elif option == 3:
                number = int(input("Please enter the number of participants: "))
                theme = input("Please enter the theme of the project: ")
                repo.limit_number_by_theme(number, theme)
                print(repo)
            elif option == 4:
                print(repo)
            elif option == 0:
                print("Thank you for using the project manager!")
                return
            else:
                print("Invalid option")
        except ValueError as ve:
            print(ve)
        except TypeError as te:
            print(te)
