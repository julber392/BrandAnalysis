from abc import ABC, abstractmethod
from typing import List, Dict


class DataReaderBase(ABC):
    """Абстрактный базовый класс для чтения данных."""

    @abstractmethod
    def read(self, files: List[str]) -> List[Dict[str, str]]:
        """Считывает данные из файлов и возвращает список строк."""
        pass
