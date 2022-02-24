
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def catchPhrase(self):
        msg = "Yo"
        return msg


class Employee(Person):
    ID = 0




if __name__ == "__main__":

    p1 = Person("Carson", 24)

    print(p1.name)
    print(p1.age)
    print(p1.catchPhrase())
