class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, *nums):

        for num in nums:
            self.result += num

        print(self.result)


a = Calculator()

#a.add(5, 9, 4, 4, 1, 2, 2)


b = {"a": 1, "c": 2}

print(b['a'])
print(b.a)