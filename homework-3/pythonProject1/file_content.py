class BaseContent:
    def __init__(self, content_bytes=None):
        self._content_bytes = content_bytes
        self._size = self._size_of(content_bytes)

    @property
    def size(self):
        return self._size

    @property
    def content_bytes(self):
        return self._content_bytes

    @content_bytes.setter
    def content_bytes(self, content_bytes):
        self._content_bytes = content_bytes
        self._size = self._size_of(content_bytes or 0)

    def _size_of(self, content):
        # Реализация, которая умеет считать размер байтов. Для тестового задания реализация не требуется
        pass

    # Метод, который должны реализовать дочерние объекты
    def _to_bytes(self, *args):
        pass


class TextContent(BaseContent):
    def __init__(self, text):
        super().__init__(self._to_bytes(text))
        self._text = text

    def _to_bytes(self, text):
        # Реализация, которая умеет переводить объект Text в байты. Для тестового задания реализация не требуется
        pass

    # Методы добавлены исключительно для примера работы с контентом файла
    def input_char(self, string, line, pos):
        # алгоритм, который добавляет символ в текст
        pass

    def delete_char(self, line, pos):
        # алгоритм, который удаляет символ из текста
        pass


class AudioContent(BaseContent):
    def __init__(self, audio):
        super().__init__(self._to_bytes(audio))
        self._audio = audio

    def _to_bytes(self, audio):
        # Реализация, которая умеет переводить объект Audio в байты. Для тестового задания реализация не требуется
        pass


class VideoContent(BaseContent):
    def __init__(self, audio, video):
        super().__init__(self._to_bytes(audio, video))
        self._audio = audio
        self._video = video

    def _to_bytes(self, audio, video):
        # Реализация, которая умеет переводить объект Audio и Video в байты. Для тестового задания реализация не требуется
        pass


class ImageContent(BaseContent):
    def __init__(self, image):
        super().__init__(self._to_bytes(image))
        self._image = image

    def _to_bytes(self, image):
        # Реализация, которая умеет переводить объект Image в байты. Для тестового задания реализация не требуется
        pass
