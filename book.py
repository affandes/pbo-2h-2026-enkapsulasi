from datetime import datetime

class Book:
    def __init__(self, idx, title, author):
        self.__id = idx
        self.__title = title
        self.author = author
        self.last_updated = datetime.now()

    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def set_title(self, new_title):
        if not isinstance(new_title, str):
            raise TypeError("Title harus String")
        
        if len(new_title) < 3:
            raise ValueError("Title minimal 3 karakter")

        self.__title = new_title