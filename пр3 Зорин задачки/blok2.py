import math

def ierarhy():
    class Employee:
        def __init__(self, name, salary):
            self.name=name
            self.salary=salary

        def income(self):
            return self.salary

        def info(self):
            return f"{self.name}: доход {self.income():.0f} руб."

    class Manager(Employee):
        def __init__(self, name, salary, bonus):
            super().__init__(name, salary)
            self.bonus=bonus

        def income(self):
            return super().income()+self.bonus

    class Developer(Employee):
        def __init__(self, name, salary, level):
            super().__init__(name, salary)
            self.level=level

        def income(self):
            k={1: 1.0, 2: 1.2, 3: 1.5}.get(self.level, 1.0)
            return self.salary*k

    class Intern(Employee):
        def __init__(self, name, hourly_rate, hours):
            super().__init__(name, 0)
            self.hourly_rate=hourly_rate
            self.hours=hours

        def income(self):
            return self.hourly_rate*self.hours

    return Employee, Manager, Developer, Intern

def z6():
    print("Задание 6")
    Employee, Manager, Developer, Intern=ierarhy()

    staff=[
        Manager("Анна", 80000, 15000),
        Developer("Антон", 70000, 3),
        Intern("Коля", 500, 80),
        Employee("Глеб", 60000),
    ]
    for employee in staff:
        print(employee.info())

    total=sum(e.income() for e in staff)
    print(f"Суммарный доход: {total:.0f} руб.")

def z7():
    print("Задание 7")
    class Product:
        def __init__(self, name, price):
            self.name=name
            self.price=price

    class BrokenDiscountedProduct(Product):
        def __init__(self, name, price, discount):
            self.discount=discount

    try:
        broken=BrokenDiscountedProduct("Ноутбук", 50000, 10)
        print(broken.name)
    except AttributeError as error:
        print("Перехвачен AttributeError:", error)

    class DiscountedProduct(Product):
        def __init__(self, name, price, discount):
            super().__init__(name, price)
            self.discount=discount

    fixed=DiscountedProduct("Ноутбук", 50000, 10)
    print(f"{fixed.name}: {fixed.price} руб., скидка {fixed.discount}%")

def z8():
    print("Задание 8")
    class Vehicle:
        def __init__(self, brand, model):
            self.brand=brand
            self.model=model

        def describe(self):
            return f"Транспорт: {self.brand} {self.model}"

    class Car(Vehicle):
        def __init__(self, brand, model, doors):
            super().__init__(brand, model)
            self.doors=doors

        def describe(self):
            return super().describe()+f", дверей: {self.doors}"

    class Bicycle(Vehicle):
        def __init__(self, brand, model, frame_type):
            super().__init__(brand, model)
            self.frame_type=frame_type

        def describe(self):
            return super().describe()+f", рама: {self.frame_type}"

    vehicles=[
        Car("Lada", "Vesta", 4),
        Car("Ford", "Focus", 5),
        Bicycle("Stels", "Navigator", "горная"),
        Bicycle("Forward", "Apache", "шоссейная"),
    ]
    for vehicle in vehicles:
        print(vehicle.describe())

def z9():
    print("Задание 9")
    class Point2D:
        def __init__(self, x, y):
            self.x=x
            self.y=y

        def distance_to(self, other):
            return math.hypot(self.x-other.x, self.y-other.y)

        def __str__(self):
            return f"Point ({self.x}; {self.y})"

    class Point3D(Point2D):
        def __init__(self, x, y, z):
            super().__init__(x, y)
            self.z=z

        def distance_to(self, other):
            return math.sqrt(
                (self.x-other.x)**2
                +(self.y-other.y)**2
                +(self.z-other.z)**2
            )

        def __str__(self):
            base=super().__str__()
            return base[:-1]+f"; {self.z})"

    a=Point2D(0, 0)
    b=Point2D(3, 4)
    c=Point3D(0, 0, 0)
    d=Point3D(1, 2, 2)

    print(a, "->", b, "=", a.distance_to(b))
    print(c, "->", d, "=", c.distance_to(d))

def z10():
    print("Задание 10")
    class Rectangle:
        def __init__(self, width, height):
            self.width=width
            self.height=height

        def area(self):
            return self.width*self.height

        def perimeter(self):
            return 2*(self.width + self.height)

    class Square(Rectangle):
        def __init__(self, side):
            super().__init__(side, side)

    square=Square(5)
    print("Площадь:", square.area())
    print("Периметр:", square.perimeter())
    print("isinstance(square, Rectangle):", isinstance(square, Rectangle))

def main():
    tasks=[z6, z7, z8, z9, z10]
    for task in tasks:
        print("\n")
        task()

if __name__=="__main__":
    main()