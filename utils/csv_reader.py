import csv
from typing import List, Dict
from .base import DataReaderBase


class CsvReader(DataReaderBase):
    def read(self, files: List[str]) -> List[Dict[str, str]]:
        all_rows = []
        for file_path in files:
            try:
                with open(file_path, encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    all_rows.extend(reader)
            except FileNotFoundError:
                print(f"Файл не найден по пути {file_path}")
        return all_rows
