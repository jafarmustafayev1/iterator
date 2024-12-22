class FibonacciIterator:
    def __init__(self, count):
        self.count = count
        self.current = 0
        self.next = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration
        result = self.current
        self.current, self.next = self.next, self.current + self.next
        self.index += 1
        return result

class FibonacciCalculator:
    def __init__(self, count):
        self.numbers = list(FibonacciIterator(count))

    def calculate_sum(self):
        return sum(self.numbers)

    def calculate_average(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def display_results(self):
        print("Fibonacci sonlari:", self.numbers)
        print("Jami yig'indisi:", self.calculate_sum())
        print("O'rtacha qiymat:", self.calculate_average())

calculator = FibonacciCalculator(10)
calculator.display_results()
