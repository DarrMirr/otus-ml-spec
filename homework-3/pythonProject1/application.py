from file_managed import BaseFileManaged


class BaseApplication:
    def __init__(self):
        self._opened_files = dict([])

    def open_file(self, file_managed: BaseFileManaged):
        self._opened_files[file_managed.file.name] = file_managed

    def close_file(self, file_name):
        del self._opened_files[file_name]

    def save_file(self, file_name, path):
        self._opened_files[file_name].copy_to(path)


class NotePad(BaseApplication):

    # Методы добавлены исключительно для примера работы с контентом файла
    def input_char(self, file_name, char, line, pos):
        self._opened_files[file_name].file.content.input_char(char, line, pos)

    def delete_char(self, file_name, line, pos):
        content = self._opened_files[file_name].file.content.delete_char(line, pos)


class ImageViewer(BaseApplication):
    pass


class VideoPlayer(BaseApplication):
    pass


class AudioPlayer(BaseApplication):
    pass
