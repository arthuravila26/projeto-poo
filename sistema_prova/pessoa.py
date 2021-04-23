class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__sobrenome = ""
        self.__idade = 0
        self.__id = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def idade(self):
        return self.__idade

    @property
    def id(self):
        return self.__id
