from tkinter import Tk, Entry, Button, Frame, Label, StringVar, END
from logic import (
    plus, minus, umnozh, delenie, step, kore, factorial,
    Memory, CalculatorError
)

class CalculatorApp:
    def __init__(self):
        self.memory=Memory()
        self.wnd=Tk()
        self.wnd.title("Калькулятор")
        self.wnd.geometry("320x420")
        self.wnd.resizable(False, False)

        self.expr=StringVar()
        self.sozd_display()
        self.sozd_knopki()

    def sozd_display(self):
        display=Entry(self.wnd, textvariable=self.expr, font=("Arial", 18),
                        justify="right")
        display.place(x=10, y=10, width=300, height=50)

    def sozd_knopki(self):
        panel=Frame(self.wnd, bd=3, relief="groove")
        panel.place(x=10, y=70, width=300, height=340)

        layout=[
            ("7", lambda: self.press("7")), ("8", lambda: self.press("8")),
            ("9", lambda: self.press("9")), ("/", self.on_delenie),
            ("4", lambda: self.press("4")), ("5", lambda: self.press("5")),
            ("6", lambda: self.press("6")), ("*", self.on_umnozh),
            ("1", lambda: self.press("1")), ("2", lambda: self.press("2")),
            ("3", lambda: self.press("3")), ("-", self.on_minus),
            ("0", lambda: self.press("0")), (".", lambda: self.press(".")),
            ("+", self.on_plus), ("=", self.on_ravno),
            ("x²", self.on_step), ("√", self.on_kore),
            ("n!", self.on_factorial), ("C", self.on_clear),
            ("MS", self.on_memory_save), ("MR", self.on_memory_read),
            ("M+", self.on_memory_plus), ("MC", self.on_memory_clear),
        ]

        for i, (text, cmd) in enumerate(layout):
            row, col=divmod(i, 4)
            btn=Button(panel, text=text, command=cmd,
                         font=("Arial", 12, "bold"))
            btn.place(x=5+col*72, y=5+row*55, width=66, height=50)

    def press(self, ch):
        self.expr.set(self.expr.get() + ch)

    def _get_value(self):
        try:
            return float(self.expr.get())
        except ValueError:
            raise CalculatorError("Некорректное число")

    def _show(self, value):
        if isinstance(value, float) and value.is_integer():
            value=int(value)
        self.expr.set(str(value))

    def _safe(self, func, *args):
        try:
            self._show(func(*args))
        except CalculatorError as e:
            self.expr.set(f"Ошибка: {e}")

    def on_plus(self):
        self._pending=("+", self._get_value())
        self.expr.set("")

    def on_minus(self):
        self._pending=("-", self._get_value())
        self.expr.set("")

    def on_umnozh(self):
        self._pending=("*", self._get_value())
        self.expr.set("")

    def on_delenie(self):
        self._pending=("/", self._get_value())
        self.expr.set("")

    def on_ravno(self):
        if not hasattr(self, "_pending"):
            return
        op, left=self._pending
        right=self._get_value()
        if op=="+":
            self._safe(plus, left, right)
        elif op=="-":
            self._safe(minus, left, right)
        elif op=="*":
            self._safe(umnozh, left, right)
        elif op=="/":
            self._safe(delenie, left, right)
        del self._pending

    def on_step(self):
        self._safe(step, self._get_value(), 2)

    def on_kore(self):
        self._safe(kore, self._get_value())

    def on_factorial(self):
        val=self._get_value()
        if not float(val).is_integer():
            self.expr.set("Ошибка: нужно целое число")
            return
        self._safe(factorial, int(val))

    def on_clear(self):
        self.expr.set("")

    def on_memory_save(self):
        self.memory.save(self._get_value())

    def on_memory_read(self):
        self._show(self.memory.read())

    def on_memory_plus(self):
        self.memory.add_to_memory(self._get_value())

    def on_memory_clear(self):
        self.memory.clear()

    def run(self):
        self.wnd.mainloop()

if __name__=="__main__":
    CalculatorApp().run()