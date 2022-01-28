class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top==self.get_max_size()-1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("Stack overflow")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def is_empty(self):
        if self.__top==-1:
            #print("Stack Underflow")
            return True
        return False

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            k=self.__top
            self.__top-=1
            print(f"Removed value is :{self.__elements[k]}")
    def display(self):
        if (self.is_empty()):
            print("The stack is empty")
        else:
            index = self.__top
            while (index >= 0):
                print(self.__elements[index])
                index -= 1

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while (index >= 0):
            msg.append((str)(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg


stack1 = Stack(5)
# Push all the required element(s).
stack1.push("Shirt1")
stack1.push("kishan")
stack1.push("mishra")
stack1.push("piku")
stack1.push("chiku")
stack1.push("kis")
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.display()
