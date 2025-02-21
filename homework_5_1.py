def caching_fibonacci():
    cache = {} # Empty dictionary cache
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n] # Return the cached if has already been computed

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Recursive calculation of the Fibonacci number with caching
        return cache[n]
    return fibonacci # Return the function

fib = caching_fibonacci()
print(fib(5))
print(fib(30))
print(fib(10))
print(fib(15))