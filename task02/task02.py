import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Регулярний вираз для пошуку дійсних чисел
    pattern = r'\b\d+\.\d{2}\b'
    
    # Поділяємо текст на частини для послідовного оброблення
    for part in text.split():
        if re.match(pattern, part):
            yield float(part)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total = sum(func(text))
    return total
# Запуск функції
if __name__ == "__main__":
    text = """Загальний дохід працівника складається з декількох частин: 
    1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.
    """
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")
