class add:
    def __init__(self,a,b):
        print("Inside Constructor")
        self.a=a
        self.b=b

    def __del__(self):
        print("Inside destructor")
    def cal(self):
        print("Inside Cal function")
        return self.a+self.b
    def display(self):
        print("Inside display function ")
        print(f'First number is {self.a}')
        print(f"Secod NUmber is {self.b}")
        print(f"Result is {self.cal()}")


print("Creating object")
ob=add(5,2)
ob.display()
print("Program ended ")
