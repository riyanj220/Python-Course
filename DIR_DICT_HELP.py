# l = (1, 2, 3, 4)
# print(
#     dir(l)
# )  # jitny b methods aur attributes is tuple k saath use ho sakty hy ye wo sab bata dega

# dictionary = {"name": "riyan", "age": 18, "city": "karachi"}
# print(dictionary["name"])
# print(dictionary["age"])

# help(tuple)
# ___________________________________________________________________________


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.height = 5


p = person("riyan", 20)
print(
    p.__dict__
)  # hamne jitny b attribute set kiye hy wo hame dictionary ki form me mil jayge
