import random

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

class FibonacciGuessGame:
    def __init__(self, count):
        self.fibonacci_numbers = list(FibonacciIterator(count))

    def play(self):
        print("Fibonacci o'yiniga xush kelibsiz!")
        print("Qator ichidan Fibonacci sonini topishingiz kerak.")
        print(f"Masalan: {self.fibonacci_numbers}\n")

        target = random.choice(self.fibonacci_numbers)
        for attempt in range(3):
            try:
                guess = int(input(f"{attempt + 1}-urinish: Fibonacci sonini kiriting: "))
                if guess == target:
                    print("Tabriklaymiz! Siz Fibonacci sonini topdingiz!")
                    return
                else:
                    print("Noto'g'ri. Yana harakat qilib ko'ring.")
            except ValueError:
                print("Faqat raqam kiriting!")

        print(f"Kechirasiz, siz topa olmadingiz. To'g'ri javob: {target}")

game = FibonacciGuessGame(10)
game.play()
