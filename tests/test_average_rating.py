import pytest
from reports.average_rating import AverageRatingReport

@pytest.fixture
def sample_data():
    """Пример данных для тестов."""
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "iphone 14", "brand": "apple", "price": "899", "rating": "4.7"},
        {"name": "galaxy s23", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.6"},
    ]


def test_average_rating_correct_calculation(sample_data):
    """Проверяем корректный расчёт среднего рейтинга."""
    report = AverageRatingReport()
    result = report.generate(sample_data)

    brands = [r[0] for r in result]
    assert set(brands) == {"Apple", "Samsung", "Xiaomi"}

    assert result[0][0] == "Apple"

    apple_row = next(r for r in result if r[0] == "Apple")
    assert apple_row[1] == pytest.approx(4.8, 0.01)


def test_average_rating_ignores_invalid_rows():
    """Проверяем, что некорректные строки (без бренда или рейтинга) пропускаются."""
    bad_data = [
        {"name": "iphone", "brand": "", "rating": "4.9"},
        {"name": "galaxy", "brand": "samsung", "rating": ""},
        {"name": "redmi", "price": "100", "rating": "4.5"},
    ]
    report = AverageRatingReport()
    result = report.generate(bad_data)
    assert result == []

def test_average_rating_case_insensitive(sample_data):
    """Проверяем, что названия брендов не зависят от регистра."""
    modified = sample_data + [
        {"name": "IPHONE 13", "brand": "Apple", "price": "799", "rating": "4.5"},
        {"name": "iphone se", "brand": "APPLE", "price": "499", "rating": "4.4"},
    ]
    report = AverageRatingReport()
    result = report.generate(modified)

    assert len(result) == 3
    brands = [r[0] for r in result]
    assert "Apple" in brands


def test_average_rating_empty_input():
    """Проверяем, что при пустых данных возвращается пустой список."""
    report = AverageRatingReport()
    result = report.generate([])
    assert result == []


def test_average_rating_sorting_order(sample_data):
    """Проверяем, что бренды отсортированы по убыванию рейтинга."""
    report = AverageRatingReport()
    result = report.generate(sample_data)

    ratings = [r[1] for r in result]
    assert ratings == sorted(ratings, reverse=True)
