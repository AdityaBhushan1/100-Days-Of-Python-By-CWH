# class Person:
#     name = "Aditya"
#     occ = "OWNER"

#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a= Person()
# a.info()

# a.name = "Divya"
# a.occ = "HR"


class Person:
    def __init__(self,n,o) -> None: # Always Executed When a Class is called
        print("Hey I am A Person") 
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Aditya","Developer")
a.info()
b = Person("Ananya","HR")
b.info()
# b = Person("Ananya","HR","1000") # gives error 
