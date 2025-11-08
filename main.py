import argparse
from tabulate import tabulate
from utils.csv_reader import CsvReader
from reports.average_rating import AverageRatingReport

REPORTS = {
    "average-rating": AverageRatingReport
}


def main():
    parser = argparse.ArgumentParser(description="Анализ рейтинга брендов")
    parser.add_argument("--files", nargs="+", required=True, help="пути к CSV-файлам")
    parser.add_argument("--report", required=True, help="название отчёта (например: average-rating)")
    args = parser.parse_args()

    if args.report not in REPORTS:
        print(f"Неизвестный отчёт '{args.report}'. Доступные: {', '.join(REPORTS.keys())}")
        return

    reader = CsvReader()
    rows = reader.read(args.files)
    if not rows:
        print("Нет данных для анализа.")
        return

    report = REPORTS[args.report]()
    result = report.generate(rows)

    print(tabulate(result, headers=["Бренд", "Средний рейтинг"], tablefmt="github"))


if __name__ == "__main__":
    main()
