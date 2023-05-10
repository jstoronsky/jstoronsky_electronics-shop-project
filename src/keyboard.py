from src.item import Item


class KeyboardLanguage:
    def __init__(self, default_language="EN"):
        self.__language = default_language

    @property
    def language(self):
        """
        позволяет получить атрибут
        """
        return self.__language

    @language.setter
    def language(self, language):
        """
        сеттер поднимает Аттрибут еррор
        """
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        """
        метод для смены раскладки
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, KeyboardLanguage):
    pass
