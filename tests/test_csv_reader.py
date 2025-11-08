from utils.csv_reader import CsvReader


def test_csv_reader_reads_file(tmp_path):
    """Проверяем, что CSV читается корректно."""
    file_path = tmp_path / "test.csv"
    file_path.write_text("name,brand,price,rating\niphone,apple,1000,4.9\n")

    reader = CsvReader()
    rows = reader.read([str(file_path)])

    assert len(rows) == 1
    assert rows[0]["brand"] == "apple"
    assert rows[0]["rating"] == "4.9"


def test_csv_reader_handles_multiple_files(tmp_path):
    """Проверяем, что можно передать несколько файлов."""
    f1 = tmp_path / "a.csv"
    f2 = tmp_path / "b.csv"
    f1.write_text("name,brand,price,rating\niphone,apple,1000,4.9\n")
    f2.write_text("name,brand,price,rating\ngalaxy,samsung,1200,4.8\n")

    reader = CsvReader()
    rows = reader.read([str(f1), str(f2)])

    assert len(rows) == 2
    brands = {r["brand"] for r in rows}
    assert brands == {"apple", "samsung"}


def test_csv_reader_missing_file(capsys):
    """Проверяем, что при отсутствии файла выводится предупреждение и возвращается пустой список."""
    reader = CsvReader()
    rows = reader.read(["nonexistent.csv"])

    assert rows == []

    captured = capsys.readouterr()
    assert "Файл не найден" in captured.out


def test_csv_reader_empty_file(tmp_path):
    """Проверяем, что пустой файл не вызывает ошибок."""
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")
    reader = CsvReader()

    rows = reader.read([str(file_path)])
    assert rows == []
