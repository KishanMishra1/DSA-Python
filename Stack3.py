# lex_auth_012742584360976384939

class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if (self.__top == self.__max_size - 1):
            return True
        return False

    def is_empty(self):
        if (self.__top == -1):
            return True
        return False

    def push(self, data):
        if (self.is_full()):
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if (self.is_empty()):
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

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

def find_average(num_list):
    res=[]
    avg=0
    sum=0
    count=0
    for i in range(num_list.get_max_size()-1):
        res.append(num_list.pop())
    for i in range(len(res)):
        sum+=res[i]
        count+=1
    avg=sum/count
    for i in range(len(res)):
        num_list.push(res[::-1][i])
    num_list.push(avg)
    return num_list




# Push different values to the stack and test your program
num_list = Stack(7)
num_list.push(13)
num_list.push(14)
num_list.push(62)
num_list.push(46)
num_list.push(100)
num_list.push(71)
new_stack = find_average(num_list)

'''new_stack2=Stack(7)
while not num_list.is_empty():
    new_stack2.push(num_list.pop())
new_stack2.display()'''
