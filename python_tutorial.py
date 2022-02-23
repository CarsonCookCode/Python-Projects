
# Python:    3.7.8
#
# Author:   Carson Cook
# 
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable/
#           return variable _means that we are returning the variable to
#           back to the calling function.





def start():
    fname = "Carson"
    lname = "Cook"
    age = 24
    gender = "Male"
    get_info(fname, lname, age, gender)


def get_number():
    number = 12
    return number

def get_info(fname, lname, age, gender):
    print("My name is {} {}. I am a {} year old {}.".format(fname, lname, age, gender))

















if __name__ == "__main__":
    start()
