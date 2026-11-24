import math

def shape_ierarhy():
    class Shape:
        def __init__(self, name):
            self.name=name

        def area(self):
            return 0.0

    class Rectangle(Shape):
        def __init__(self, width, height, name="Прямоугольник"):
            super().__init__(name)
            self.width=width
            self.height=height

        def area(self):
            return self.width*self.height

    class Circle(Shape):
        def __init__(self, radius, name="Круг"):
            super().__init__(name)
            self.radius=radius

        def area(self):
            return math.pi*self.radius**2

    return Shape, Rectangle, Circle

def z11():
    print("Задание 11")
    Shape, Rectangle, Circle=shape_ierarhy()

    figures=[
        Rectangle(4, 5, "Прямоугольник 4x5"),
        Circle(2, "Круг R=2"),
        Rectangle(3, 3, "Квадрат 3x3"),
        Circle(1.5, "Круг R=1.5"),
        Shape("Абстрактная фигура"),
    ]

    for figure in sorted(figures, key=lambda f: f.area()):
        print(f"{figure.name}: {figure.area():.2f}")

    print("area() базового класса:", Shape("Фигура").area())

def z12():
    print("Задание 12")
    class Notification:
        def send(self):
            return "Базовое уведомление"

    class EmailNotification(Notification):
        def send(self):
            return "Письмо отправлено на e-mail"

    class SmsNotification(Notification):
        def send(self):
            return "SMS отправлено"

    def broadcast(messages):
        for notification in messages:
            print(notification.send())

    print("До добавления PushNotification")
    broadcast([EmailNotification(), SmsNotification()])

    class PushNotification(Notification):
        def send(self):
            return "Push-уведомление доставлено"

    print("После добавления PushNotification")
    broadcast([EmailNotification(), SmsNotification(), PushNotification()])

def z13():
    print("Задание 13")
    class Greeter:
        def hello(self):
            return "Привет!"

    class FormalGreeter(Greeter):
        def hello(self):
            return super().hello()+" Добрый день!"

        def hello_direct(self):
            return Greeter.hello(self)+" Добрый день!"

    greeter=FormalGreeter()
    print("super():", greeter.hello())
    print("Greeter.hello():", greeter.hello_direct())
    print("Результаты совпадают:", greeter.hello()==greeter.hello_direct())

def z14():
    print("Задание 14")
    class Account:
        def __init__(self, owner, balance=0.0):
            if balance<0:
                raise ValueError("Начальный баланс не может быть отрицательным")
            self.owner=owner
            self.__balance=float(balance)

        @property
        def balance(self):
            return self.__balance

        def deposit(self, amount):
            if amount<=0:
                raise ValueError("Сумма должна быть положительной")
            self.__balance+=amount

        def withdraw(self, amount):
            if amount<=0:
                raise ValueError("Сумма должна быть положительной")
            if amount>self.__balance:
                raise ValueError("Недостаточно средств")
            self.__balance-=amount

    class CreditAccount(Account):
        def __init__(self, owner, balance, limit):
            super().__init__(owner, balance)
            self.limit=limit

        def available(self):
            return self.balance+self.limit

        def try_direct_access(self):
            try:
                return self.__balance
            except AttributeError as error:
                return f"AttributeError: {error}"

    account=CreditAccount("Иванов И. И.", 10000, 5000)
    account.deposit(3000)
    account.withdraw(2000)
    print("Баланс после операций:", account.balance)
    print("Доступная сумма (баланс + лимит):", account.available())
    print("Прямое обращение к __balance:", account.try_direct_access())

    try:
        account.balance=0
    except AttributeError as error:
        print("Попытка изменить balance напрямую:", type(error).__name__)

def z15():
    print("Задание 15")
    class Person:
        def __init__(self, name):
            self.name=name

        def introduce(self):
            return f"Я {self.name}"

    class Employee(Person):
        def __init__(self, name, salary):
            super().__init__(name)
            self.salary=salary

        def introduce(self):
            return (super().introduce()+f", работаю за {self.salary} руб.")

    class Manager(Employee):
        def __init__(self, name, salary, department):
            super().__init__(name, salary)
            self.department=department

        def introduce(self):
            return (super().introduce()+f", руковожу отделом {self.department}")

    person=Person("Анна")
    employee=Employee("Борис", 70000)
    manager=Manager("Вера", 90000, "Продажи")

    for human in (person, employee, manager):
        print(human.introduce())

    print("Manager.__mro__:", Manager.__mro__)
    print("isinstance(manager, Person):", isinstance(manager, Person))
    print("issubclass(Manager, Person):", issubclass(Manager, Person))

def main():
    tasks=[z11, z12, z13, z14, z15]
    for task in tasks:
        print("\n")
        task()

if __name__=="__main__":
    main()