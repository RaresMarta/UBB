from src.Project import Project


class ProjectRepo:
    def __init__(self):
        """
        Description: Constructor for ProjectRepo class
        Input: None
        Output: None
        Error: None
        """
        self.__projects = []

    def add_project(self, project):
        """
        Description: Adds a project to the repository
        Input: project (Project)
        Output: None
        Error: TypeError if project is not a Project object
        """
        if not isinstance(project, Project):
            raise TypeError("Project must be a Project object")
        if project in self.__projects:
            raise ValueError("Project already exists")
        if project.get_name() in [project.get_name() for project in self.__projects]:
            raise ValueError("Project name already exists")
        self.__projects.append(project)

    def limit_number_by_theme(self, number, theme):
        """
        Description: Limits the number of projects by theme
        Input: number (int), theme (string)
        Output: None
        Error: TypeError if number is not an int
        """
        if number < 1:
            raise ValueError("Number must be greater than 1")
        for project in self.__projects:
            if project.get_theme() == theme:
                project.set_number(number)

    def delete_by_name(self, name):
        """
        Description: Deletes a project by name
        Input: name (string)
        Output: None
        Error: None
        """
        if name not in [project.get_name() for project in self.__projects]:
            raise ValueError("Project does not exist")
        for project in self.__projects:
            if project.get_name() == name:
                self.__projects.remove(project)
                return

    def __str__(self):
        """
        Description: Returns a string representation of the ProjectRepo object
        Input: None
        Output: string
        Error: None
        """
        return "\n".join([str(project) for project in self.__projects])
