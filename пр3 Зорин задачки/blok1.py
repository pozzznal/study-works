class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return "Какой-то звук"

    def info(self):
        return f"{self.name}: {self.speak()}"

class Dog(Animal):
    def __init__(self, name, breed="дворняга"):
        super().__init__(name)
        self.breed=breed

    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

class Cow(Animal):
    def speak(self):
        return "Му!"

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def introduce(self):
        return f"Я {self.name}, мне {self.age} лет"

class Student(Person):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group=group

    def introduce(self):
        return super().introduce()+f" Я учусь в группе {self.group}"

def z1():
    print("Задание 1")
    zoo=[Dog("Пенсель", "овчарка"), Cat("Катко"), Cow("Мумунька")]
    for animal in zoo:
        print(animal.info())

    print("isinstance(zoo[0], Animal):", isinstance(zoo[0], Animal))
    print("issubclass(Cow, Animal):", issubclass(Cow, Animal))

def z2():
    print("Задание 2")
    person=Person("Ванька", 19)
    student=Student("Данила", 20, "12-241")

    print(person.introduce())
    print(student.introduce())

    print("isinstance(person, Person):", isinstance(person, Person))
    print("isinstance(student, Person):", isinstance(student, Person))


def z3():
    print("Задание 3")
    student=Student("Данила", 20, "12-241")

    print("issubclass(Dog, Animal):", issubclass(Dog, Animal))
    print("issubclass(Student, Person):", issubclass(Student, Person))
    print("issubclass(Person, Dog):", issubclass(Person, Dog))
    print("isinstance(student, Person):", isinstance(student, Person))
    print('isinstance("текст", Person):', isinstance("текст", Person))

    print("Dog.__bases__:", Dog.__bases__)
    print("Student.__bases__:", Student.__bases__)
    print("Person.__bases__:", Person.__bases__)

def z4():
    print("Задание 4")
    class Employee:
        def __init__(self, name, salary):
            self.name=name
            self.salary=salary

        def info(self):
            return f"{self.name}: оклад {self.salary}"

    class Manager(Employee):
        def __init__(self, name, salary, department):
            super().__init__(name, salary)
            self.department=department

    manager=Manager("Анна", 80000, "Продажи")

    print(manager.info())
    print("name:", manager.name)
    print("salary:", manager.salary)
    print("department:", manager.department)


def z5():
    print("Задание 5")
    class Device:
        vendor="Acme"

        def turn_on(self):
            return f"{self.vendor}: устройство включено"

    class Laptop(Device):
        def compile(self):
            return "Код скомпилирован"

    laptop=Laptop()

    for attr in ("turn_on", "compile", "vendor"):
        print(f"hasattr(laptop, '{attr}'):", hasattr(laptop, attr))

    print("isinstance(laptop, object):", isinstance(laptop, object))

    print("Device.turn_on(laptop):", Device.turn_on(laptop))

def main():
    tasks=[z1, z2, z3, z4, z5]
    for task in tasks:
        print("\n")
        task()

if __name__=="__main__":
    main()