class Routine:
    def __init__(self, Id, name, typ, difficulty, duration):
        """
        Initializes.
        :param Id: int
        :param name: str
        :param typ: str
        :param difficulty:int
        :param duration: int
        """
        self.__id = Id
        self.__name = name
        self.__type = typ
        self.__dif = difficulty
        self.__dur = duration

    def get_dif(self):
        """
        Returns dif.
        :return:int
        """
        return self.__dif

    def get_id(self):
        """
        Returns id.
        :return: int
        """
        return self.__id

    def get_name(self):
        """
        Returns name.
        :return: str
        """
        return self.__name

    def get_dur(self):
        """
        Returns duration.
        :return: int
        """
        return self.__dur

    def get_type(self):
        """
        Returns type.
        :return: int
        """
        return self.__type

    def __str__(self):
        """Str repr.
        :return: str
        """
        return f'{self.__name} {self.__id} {self.__type} {self.__dif} {self.__dur}'

    def __repr__(self):
        """
        Memory repr.
        :return: str
        """
        return str(self)
