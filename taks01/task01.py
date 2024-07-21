
def caching_fibonacci() -> function:
    cache = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            # виводимо інформацію про читання з кешу в консоль, для відстеження
            print("reading from cache")
            return cache[n]
        else:
            # виводимо інформацію про обчимлення та запис кеш в консоль, для відстеження
            print("calculating and writing to cache")
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci

# Запуск функції
if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10))
    print(fib(15))
    print(fib(16))
