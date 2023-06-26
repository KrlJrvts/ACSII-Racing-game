from unittest import mock, TestCase
from cars import Car


class CarTest(TestCase):
    def test_when_model_is_X(self):
        self.assertEqual(Car("X", 100, 0).car_model, "X", 100, 0)
