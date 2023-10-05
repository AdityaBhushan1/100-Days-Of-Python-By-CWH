class Person:
    name = "Aditya"
    occupation = "Software Developer"
    networth = 100000000000

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()

# a.name = "Aditya Bhushan"
# a.occupation = "CEO Of Stroke Tech"
# print(a.name,a.occupation)

a.info()