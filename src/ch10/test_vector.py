from unittest import TestCase

from src.ch10.vector import Vector

vector = Vector([1,2,3,4,5])

class TestVector(TestCase):

    def test_repr(self):
        actual_repr = repr(vector)
        expected_repr = 'Vector([1, 2, 3, 4, 5])'
        assert actual_repr == expected_repr

    def test_len(self):
        assert len(vector) == 5