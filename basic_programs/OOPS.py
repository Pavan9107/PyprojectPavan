class abc:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def execute(self):
        print(self.name, self.age)
        
a = abc("kusuma",26)
a.execute()
