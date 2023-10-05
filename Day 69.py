class Employee:
    company = "Apple"
    def show(self):
        print(f"The Name Is {self.name} and Company Name Is {self.company}")

    @classmethod
    def ChangeCompany(cls,newComapny):
        cls.company = newComapny
    
e1 = Employee()
e1.name = "aditya"
e1.show()
e1.ChangeCompany("Tesla")
e1.show()
print(Employee.company)