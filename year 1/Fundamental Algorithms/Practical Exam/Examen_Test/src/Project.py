class Project:
    def __init__(self, name, theme, rep_name, number):
        """
        Description: Constructor for Project class
        Input: name (string), theme (string), rep_name (string), number (int)
        Output: None
        Error: TypeError if name, theme, rep_name are not strings or if number is not an int
        """
        number += 1
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(theme, str) or theme not in ["Sustainability", "Teaching", "Development"]:
            raise TypeError("Theme must be a string and one of the following: Sustainability, Teaching, Development")
        if not isinstance(rep_name, str):
            raise TypeError("Rep_name must be a string")
        if not isinstance(number, int) or number < 1:
            raise TypeError("Number must be an integer")
        self.name = name
        self.theme = theme
        self.rep_name = rep_name
        self.number = number

    def __str__(self):
        """
        Description: Returns a string representation of the Project object
        Input: None
        Output: string
        Error: None"""
        return (
            self.name
            + " with theme "
            + self.theme
            + " by "
            + self.rep_name
            + " and "
            + str(self.number - 1)
            + " others"
        )

    def get_name(self):
        """
        Description: Returns the name of the project
        Input: None
        Output: string
        Error: None
        """
        return self.name

    def get_number(self):
        """
        Description: Returns the number of the project
        Input: None
        Output: int
        Error: None
        """
        return self.number

    def set_number(self, number):
        """
        Description: Sets the number of the project
        Input: number (int)
        Output: None
        Error: TypeError if number is not an int
        """
        if not isinstance(number, int) or number < 1:
            raise TypeError("Number must be an integer")
        self.number = number

    def get_theme(self):
        """
        Description: Returns the theme of the project
        Input: None
        Output: string
        Error: None
        """
        return self.theme
