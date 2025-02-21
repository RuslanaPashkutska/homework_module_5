import re
from typing import  Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Generator that finds all real numbers in the text and returns then as float values.
    """
    for match in re.finditer(r'\b\d+\.\d+\b|\b\d+\b', text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Sums all numbers in the text using the generator.
    """
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")