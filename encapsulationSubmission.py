

class Person():
    def __init__(self):
        # Protected attribute
        self._name = "Unknown"
        # Private attribute
        self.__social = 1234

    def getPrivate(self):
        print(self.__social)

    def setPrivate(self, private):
        self.__social = private


carson = Person()

# We can access this protected attribute
print(carson._name)

# We can only access this private attribute through our defined function
carson.getPrivate()

