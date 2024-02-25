from application import BaseApplication
from file import BaseFile


class FileManagedAttributes:
    def __init__(self, path, datetime_create, creator):
        self._path = path
        self._datetime_create = datetime_create
        self._creator = creator
        self._deleted = False

    @property
    def path(self):
        return self._path

    @property
    def datetime_create(self):
        return self._datetime_create

    @property
    def creator(self):
        return self._creator


class BaseFileManaged:
    def __init__(self, file):
        self._file = file
        self._file_managed_attributes = self._build_attributes()

    # Система, которая управляет файлом, должна реализовать этот метод. Для тестового задания реализация метода не важна.
    def _build_attributes(self):
        return None

    @property
    def file(self) -> BaseFile:
        return self._file

    @property
    def file_managed_attributes(self) -> FileManagedAttributes:
        return self._file_managed_attributes

    def copy_to(self, path):
        # Система, которая управляет файлом, должна реализовать этот метод. Для тестового задания реализация метода не важна.
        pass

    def delete(self, is_delete_directly=False):
        # Система, которая управляет файлом, должна реализовать этот метод. Для тестового задания реализация метода не важна.
        pass

    def open_by(self, application: BaseApplication):
        application.open_file(self)

    def rename(self, name):
        self._file.name = name


# У каждой системы свои атрибуты и способы управления файлами
class FileManagedByLinux(BaseFileManaged):
    # Оставлен для примера и реализация не требуется
    pass


class FileManagedByWindows(BaseFileManaged):
    # Оставлен для примера и реализация не требуется
    pass


class FileManagedByS3(BaseFileManaged):
    # Оставлен для примера и реализация не требуется
    pass
