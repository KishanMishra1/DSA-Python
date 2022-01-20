'''let’s say you wanted to track the number of dogs
that may have different attributes like breed, age.
If a list is used, the first element could be the dog’s breed
while the second element could represent its age.
Let’s suppose there are 100 different dogs,
then how would you know which element is supposed to be which?
What if you wanted to add other properties to these dogs?
This lacks organization and it’s the exact need for classes.

Class creates a user-defined data structure,
which holds its own data members and member functions,
which can be accessed and used by creating an instance of that class.
A class is like a blueprint for an object.'''


# Class for Dog
class Dog:
    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):
        # Instance Variable
        self.breed = breed
        self.color = color

    # Objects of Dog class


Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)       
