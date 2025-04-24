from resumex.core.di import Provider
from resumex.core.services import FileService


class ServiceProvider(Provider):

    @property
    def file_service(self) -> FileService:
        return self._file_service

    def __init__(self):
        super().__init__()
        self._file_service = FileService()
