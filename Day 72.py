class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("aditya")
    def child_method(self):
        print("This is the child method.")
        self.parent_method()
        super().parent_method()

child_object = ChildClass()
child_object.child_method()

class ParentClass1:
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

class ParentClass2:
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

class ChildClass(ParentClass1, ParentClass2):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()