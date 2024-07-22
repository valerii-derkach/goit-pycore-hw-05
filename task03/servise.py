from collections import Counter

# Функція яка парсить рядок логу в словник
def parse_log_line(line: str) -> dict[str, str]:
    # Розбиваємо по пробілу 3 рази від початку строки, тобто на 4 частини
    parts = line.split(' ', 3)
    # Якщо інформація в рядку логу неповна
    if len(parts) < 4:
        return None

    date, time, level, message = parts

    return {
        'date': date,
        'time': time,
        'level': level,
        'message': message
    }

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list[dict[str, str]]:
    logs = []
    try:
        # Відкриваємо файл, читаємо та парсимо кожен рядок логів і зберігаємо результати в список
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line)
                if parsed_line:
                    logs.append(parsed_line)

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        return

    except Exception as e:
        print(f"Виникла помилка під час читання файлу: {e}")

    return logs

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list[dict[str, str]], level: str) -> list[dict[str, str]]:
    return list(filter(lambda log: log['level'].lower() == level.lower(), logs))

# Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: list[dict[str, str]]) -> dict[str, int]:
    log_levels = [log['level'] for log in logs]
    return dict(Counter(log_levels))

# Функція для форматування та виведення результатів у вигляді таблиці
def display_log_counts(counts: dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")
