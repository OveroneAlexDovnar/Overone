class Advertisment:
    def __init__(self, title, description, author, dateandtime, numviews):
        self.__title = title
        self.__description = description
        self.__author = author
        self.__dateandtime = dateandtime
        self.__numviews = numviews

    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
    def get_author(self):
        return self.__author
    def get_dateandtime(self):
        return self.__dateandtime
    def get_numviews(self):
        return self.__numviews

    def __str__(self):
        return f'title - {self.__title}, description - {self.__description}, author - {self.__author}, dateandtime - {self.__dateandtime}, numviews -{self.__numviews}'
