import unittest
from main import variant6

class TestVariant6(unittest.TestCase):
    def test_operator_coverage(self):
        # Тестування покриття операторів
        self.assertEqual(variant6(False, 11, 20, 100), 267)  # Тест-кейс 1
        self.assertEqual(variant6(False, 10, 20), 267)  # Тест-кейс 2
        self.assertEqual(variant6(True, 11, 12, 100), 267)  # Тест-кейс 3

    def test_decision_coverage(self):
        # Тестування покриття рішень
        self.assertEqual(variant6(True, 15, 25, 150), 267)  # Тест-кейс 1
        self.assertEqual(variant6(False, 11, 20, 150), 267)  # Тест-кейс 2
        self.assertEqual(variant6(True, 11, 12, 150), 267)  # Тест-кейс 3

    def test_condition_coverage(self):
        # Тестування покриття умов
        self.assertEqual(variant6(True, 15, 25), 238)  # Тест-кейс 1
        self.assertEqual(variant6(True, 15, 25, 150), 267)  # Тест-кейс 2
        self.assertEqual(variant6(False, 15, 25, 150), 267)  # Тест-кейс 3

if __name__ == '__main__':
    unittest.main()
