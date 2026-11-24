from blok2 import ierarhy
from blok3 import shape_ierarhy

def z16():
    print("Задание 16")
    Employee, Manager, Developer, Intern=ierarhy()

    staff=[
        Manager("Анна", 80000, 15000),
        Developer("Антон", 70000, 3),
        Developer("Кирилл", 65000, 2),
        Intern("Денис", 500, 100),
        Employee("Никита", 55000),
        Manager("Женя", 95000, 20000),
    ]

    total=sum(e.income() for e in staff)
    average=total/len(staff)
    best=max(staff, key=lambda e: e.income())
    above_average=[e for e in staff if e.income()>average]

    print(f"Фонд оплаты труда: {total:.0f} руб.")
    print(f"Максимальный доход: {best.info()}")
    print(f"Доход выше среднего ({average:.0f} руб.): {len(above_average)}")
    print("Ведомость")
    for e in staff:
        print(e.info())

def z17():
    print("Задание 17")
    Shape, Rectangle, Circle=shape_ierarhy()

    figures=[
        Rectangle(4, 5, "Прямоугольник 4x5"),
        Circle(2, "Круг R=2"),
        Rectangle(3, 3, "Квадрат 3x3"),
        Circle(1.5, "Круг R=1.5"),
        Rectangle(10, 2, "Прямоугольник 10x2"),
        Circle(3, "Круг R=3"),
        Rectangle(1, 8, "Прямоугольник 1x8")
    ]

    print("По убыванию площади")
    for figure in sorted(figures, key=lambda f: f.area(), reverse=True):
        print(f"{figure.name}: {figure.area():.2f}")

    total=sum(f.area() for f in figures)
    largest=max(figures, key=lambda f: f.area())
    circles=sum(1 for f in figures if isinstance(f, Circle))
    rectangles=sum(1 for f in figures if isinstance(f, Rectangle))

    print(f"Суммарная площадь: {total:.2f}")
    print(f"Самая большая фигура: {largest.name} "
          f"({largest.area():.2f})")
    print("Кругов:", circles)
    print("Прямоугольников:", rectangles)

def z18():
    print("Задание 18")
    class LibraryItem:
        def __init__(self, title, year):
            self.title=title
            self.year=year

        def describe(self):
            return f"{self.title} ({self.year})"

    class Book(LibraryItem):
        def __init__(self, title, year, author, pages):
            super().__init__(title, year)
            self.author=author
            self.pages=pages

        def describe(self):
            return (super().describe()+f", {self.author}, {self.pages} с.")

    class Magazine(LibraryItem):
        def __init__(self, title, year, issue, month):
            super().__init__(title, year)
            self.issue=issue
            self.month=month

        def describe(self):
            return super().describe()+f", № {self.issue}, {self.month}"

    class Library:
        def __init__(self):
            self.__items=[]

        def add_item(self, item):
            if not isinstance(item, LibraryItem):
                raise TypeError("В библиотеку можно добавлять только LibraryItem")
            self.__items.append(item)

        def show_all(self):
            for item in self.__items:
                print(item.describe())

        def count_by_class(self, cls):
            return sum(1 for item in self.__items
                       if isinstance(item, cls))

    library=Library()
    library.add_item(Book("Война и мир", 1873, "Л. Н. Толстой", 1225))
    library.add_item(Book("Мастер и Маргарита", 1967, "М. А. Булгаков", 480))
    library.add_item(Book("Преступление и наказание", 1866, "Ф. М. Достоевский", 671))
    library.add_item(Magazine("Наука и жизнь", 2024, 5, "май"))
    library.add_item(Magazine("Вокруг света", 2024, 7, "июль"))

    print("Все материалы")
    library.show_all()
    print("Книг в библиотеке:", library.count_by_class(Book))

    try:
        library.add_item("не материал")
    except TypeError as error:
        print("Перехвачен TypeError:", error)

def main():
    tasks=[z16, z17, z18]
    for task in tasks:
        print("\n")
        task()

if __name__=="__main__":
    main()