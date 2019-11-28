import math
from unittest import TestCase

import pytest

from src.ch09.vector2d_v0 import Vector2d

vector = Vector2d(3.15, -8.32)


class TestVector2d(TestCase):

    def test_x(self):
        assert vector.x == 3.15

    def test_y(self):
        assert vector.y == -8.32

    def test_angle(self):
        assert math.isclose(vector.angle(), 2.7796645145331307)

    def test_read_only_properties(self):
        with pytest.raises(AttributeError):
            vector.x = 12
        with pytest.raises(AttributeError):
            vector.y = 13

    def test_hashcode(self):
        vector2 = Vector2d(3.15, -8.32)
        assert vector == vector2
        assert vector.__hash__() == vector2.__hash__()

        vector_set = {vector, vector2}
        assert len(vector_set) == 1
