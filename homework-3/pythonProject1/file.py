from file_content import BaseContent


# При создании файла нужно обязательно указать два типа name и content.
# Внутри, content может быть пустой, но сам объект должен быть обязательно передан при создании файла.
# По этой причине же ссылку на контент нельзя поменять, только состояние самого объекта content.
class BaseFile:
    def __init__(self, name: str, content: BaseContent):
        self._name = name
        self._content = content

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def content(self):
        return self._content


class FileText(BaseFile):
    pass


class FileVideo(BaseFile):
    pass


class FileAudio(BaseFile):
    pass


class FileImage(BaseFile):
    pass
