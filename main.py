class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.a, self.b = 0, 1
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count >= self.max_count:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current_count += 1
        return result

fib = FibonacciIterator(10)
print("Fibonacci sonlari:")
for num in fib:
    print(num)
