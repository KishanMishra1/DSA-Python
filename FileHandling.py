'''The number of files that can be simultaneously opened by a program is limited. So it is very important to close all the files, once the operations are completed.'''
flight_file=open("flight.txt","w")
flight_file.write("Hello")
flight_file.close()

'''Sometimes, we may encounter exceptions when dealing with files.
In this example, we are trying to write to a file which is opened in read-only mode. This will result in an exception.
In such a case, let’s see how we can use try except block to catch this exception.'''

try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")
    flight_file.close()
except:
    print("Error occurred")
    if flight_file.closed:
        print("File is closed")
    else:
        print("File is open")
'''When we want to write a code that will run in all situations, we can put it in a finally block.
Since closing a file is necessary we can do it in the finally block instead of in the try block.'''

try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")
except:
    print("Error occurred")
finally:
    print("File is being closed")
    flight_file.close()
    if flight_file.closed:
        print("File is closed")
    else:
        print("File is open")
#copy and explore
try:
    hello_file=open("flight.txt","w")
    text="Hello everyone! Welcome"
    hello_file.write(text)
except:
    print("Error occurred, not able to write to file")
finally:
    hello_file.close()
try:
    hello_file=open("flight.txt","r")
    text_from_file=hello_file.read()
    print(text_from_file)
except:
    print("Error Occurred, not able to read from file")
finally:
    hello_file.close()
