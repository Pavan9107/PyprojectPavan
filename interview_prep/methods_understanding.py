from abc import ABC, abstractmethod


class check:
    name = "pavan"

    def __init__(self, age):
        self.age = age

    def search_myname(self):   #instance method
        print(self.name)
        print(self.age)

    @classmethod
    def search_classname(cls):
        print(cls.name)

    @staticmethod
    def double_my_age(x):
        print(x*2)

    @abstractmethod
    def ABC(self):
        pass



c=check(29)
c.search_myname()
check.search_classname()
check.double_my_age(28)
