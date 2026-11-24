import unittest
from logic import (
    plus, minus, umnozh, delenie, step, kore, factorial,
    Memory, CalculatorError
)

class TestBasicOperations(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(plus(2, 3), 5)
        self.assertEqual(plus(-1, 1), 0)
        self.assertAlmostEqual(plus(0.1, 0.2), 0.3, places=7)

    def test_minus(self):
        self.assertEqual(minus(10, 4), 6)
        self.assertEqual(minus(0, 5), -5)

    def test_umnozh(self):
        self.assertEqual(umnozh(3, 4), 12)
        self.assertEqual(umnozh(-2, 5), -10)
        self.assertEqual(umnozh(0, 100), 0)

    def test_delenie(self):
        self.assertEqual(delenie(10, 2), 5)
        self.assertAlmostEqual(delenie(1, 3), 0.3333333, places=6)

    def test_delenie_on_zero(self):
        with self.assertRaises(CalculatorError):
            delenie(5, 0)

class TestPowerAndRoot(unittest.TestCase):
    def test_step(self):
        self.assertEqual(step(2, 10), 1024)
        self.assertEqual(step(2, 0), 1)
        self.assertEqual(step(9, 0.5), 3)

    def test_kore(self):
        self.assertEqual(kore(16), 4)
        self.assertEqual(kore(0), 0)

    def test_kore_negative(self):
        with self.assertRaises(CalculatorError):
            kore(-4)

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(CalculatorError):
            factorial(-3)

    def test_factorial_not_celoe(self):
        with self.assertRaises(CalculatorError):
            factorial(3.5)

class TestMemory(unittest.TestCase):
    def setUp(self):
        self.mem=Memory()

    def test_initial_state(self):
        self.assertEqual(self.mem.read(), 0)

    def test_save_and_read(self):
        self.mem.save(42)
        self.assertEqual(self.mem.read(), 42)

    def test_add_to_memory(self):
        self.mem.save(10)
        self.mem.add_to_memory(5)
        self.assertEqual(self.mem.read(), 15)

    def test_clear(self):
        self.mem.save(99)
        self.mem.clear()
        self.assertEqual(self.mem.read(), 0)

    def test_save_overwrites(self):
        self.mem.save(1)
        self.mem.save(2)
        self.assertEqual(self.mem.read(), 2)

if __name__=="__main__":
    unittest.main()