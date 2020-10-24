import datetime

class Advertisment:
    def __init__(self, title, description, author, dateandtime, numviews):
        self.__title = title
        self.__description = description
        self.__author = author
        self.__dateandtime = datetime.datetime.today()
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

    def title_change(self, new_title):
        if type(new_title) == str:
            self.__title = new_title
            return True
        return

    def description_change(self, new_description):
        if type(new_description) == str:
            self.__description = new_description
            return True
        return False

    def output(self, output_advertisment):
        self.__numviews += 1
        return True

    def __str__(self):
        return f'title - {self.__title}, description - {self.__description}, author - {self.__author}, dateandtime - {self.__dateandtime}, numviews -{self.__numviews}'




