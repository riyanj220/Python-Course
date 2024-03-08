class math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod  # ye ik normal method ki trh hi hota but independant hota object ke
    def add(a, b):
        return a + b


# a = math(5)
# print(a.num)
# a.add_to_num(6)
# print(a.num)

result = math.add(25, 30)  # static ko aap class ke name se b call kr skty hy
print(result)
