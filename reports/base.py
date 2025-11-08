from typing import List, Dict
from abc import ABC, abstractmethod


class ReportBase(ABC):
    """Абстрактный базовый класс для всех отчётов."""
    name: str = ""

    @abstractmethod
    def generate(self, rows: List[Dict[str, str]]):
        """Метод должен возвращать данные отчёта."""
        pass
