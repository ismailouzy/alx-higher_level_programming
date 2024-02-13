#!/usr/bin/python3
"""unittests for rectangle.py.

"""
import os
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle as MyRectangle
from io import StringIO
from unittest.mock import patch


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the MyRectangle class."""

    def test_my_rectangle_is_base(self):
        self.assertIsInstance(MyRectangle(10, 2), Base)

    def test_my_no_args(self):
        with self.assertRaises(TypeError):
            MyRectangle()

    def test_my_one_arg(self):
        with self.assertRaises(TypeError):
            MyRectangle(1)

    def test_my_two_args(self):
        r1 = MyRectangle(10, 2)
        r2 = MyRectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_my_three_args(self):
        r1 = MyRectangle(2, 2, 4)
        r2 = MyRectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_my_four_args(self):
        r1 = MyRectangle(1, 2, 3, 4)
        r2 = MyRectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_my_five_args(self):
        self.assertEqual(7, MyRectangle(10, 2, 0, 0, 7).id)

    def test_my_more_than_five_args(self):
        with self.assertRaises(TypeError):
            MyRectangle(1, 2, 3, 4, 5, 6)

    def test_my_width_private(self):
        with self.assertRaises(AttributeError):
            print(MyRectangle(5, 5, 0, 0, 1).__width)

    def test_my_height_private(self):
        with self.assertRaises(AttributeError):
            print(MyRectangle(5, 5, 0, 0, 1).__height)

    def test_my_x_private(self):
        with self.assertRaises(AttributeError):
            print(MyRectangle(5, 5, 0, 0, 1).__x)

    def test_my_y_private(self):
        with self.assertRaises(AttributeError):
            print(MyRectangle(5, 5, 0, 0, 1).__y)

    def test_my_width_getter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_my_width_setter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_my_height_getter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_my_height_setter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_my_x_getter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_my_x_setter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_my_y_getter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_my_y_setter(self):
        r = MyRectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangleWidth(unittest.TestCase):
    """Unittests for testing initialization of MyRectangle width attribute."""

    def test_None_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(None, 2)

    def test_str_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle("invalid", 2)

    def test_float_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(5.5, 1)

    def test_complex_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(complex(5, 3), 2)

    def test_list_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle([5, 2], 1)

    def test_dict_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle({"a": 5, "b": 2}, 1)

    def test_bool_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(True, 1)

    def test_set_my_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle({5, 2}, 1)

    def test_my_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            MyRectangle(0, 1)

    def test_negative_my_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            MyRectangle(-5, 1)

    def test_valid_my_width(self):
        r = MyRectangle(10, 2)
        self.assertEqual(r.width, 10)

class TestRectangleHeight(unittest.TestCase):
    """Unittests for testing initialization of MyRectangle height attribute."""

    def test_None_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, None)

    def test_str_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, "invalid")

    def test_float_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, 5.5)

    def test_complex_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, complex(5, 3))

    def test_list_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, [5, 2])

    def test_dict_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, {"a": 5, "b": 2})

    def test_bool_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, True)

    def test_set_my_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, {5, 2})

    def test_my_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            MyRectangle(5, 0)

    def test_negative_my_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            MyRectangle(5, -5)

    def test_valid_my_height(self):
        r = MyRectangle(5, 10)
        self.assertEqual(r.height, 10)

class TestRectangleXAndY(unittest.TestCase):
    """Unittests for testing initialization of MyRectangle x and y attributes."""

    def test_None_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(None, 5)

    def test_str_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle("invalid", 5)

    def test_float_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(5.5, 5)

    def test_complex_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(complex(5, 3), 5)

    def test_list_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle([5, 2], 5)

    def test_dict_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle({"a": 5, "b": 2}, 5)

    def test_bool_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle(True, 5)

    def test_set_my_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            MyRectangle({5, 2}, 5)

    def test_None_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, None)

    def test_str_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, "invalid")

    def test_float_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, 5.5)

    def test_complex_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, complex(5, 3))

    def test_list_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, [5, 2])

    def test_dict_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, {"a": 5, "b": 2})

    def test_bool_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, True)

    def test_set_my_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            MyRectangle(5, {5, 2})

class TestRectangleArea(unittest.TestCase):

    def test_area_small_dimensions(self):
        rectangle = MyRectangle(3, 7)
        expected_area = 3 * 7
        self.assertEqual(rectangle.area(), expected_area)

    def test_area_large_dimensions(self):
        rectangle = MyRectangle(999, 888)
        expected_area = 999 * 888
        self.assertEqual(rectangle.area(), expected_area)

    def test_area_after_dimensions_change(self):
        rectangle = MyRectangle(4, 12, 2, 2, 2)
        rectangle.width = 8
        rectangle.height = 6
        expected_area = 8 * 6
        self.assertEqual(rectangle.area(), expected_area)

    def test_area_invalid_argument(self):
        rectangle = MyRectangle(5, 9, 1, 1, 1)
        with self.assertRaises(TypeError):
            rectangle.area(1)

class TestRectangleToDictionary(unittest.TestCase):

    def test_to_dictionary(self):
        rectangle = MyRectangle(5, 10, 2, 3, 4)
        expected_dict = {'id': 4, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertDictEqual(rectangle.to_dictionary(), expected_dict)

    def test_to_dictionary_after_changes(self):
        rectangle = MyRectangle(8, 6, 1, 1, 7)
        rectangle.width = 12
        rectangle.height = 9
        rectangle.x = 3
        rectangle.y = 4
        rectangle.id = 10
        expected_dict = {'id': 10, 'width': 12, 'height': 9, 'x': 3, 'y': 4}
        self.assertDictEqual(rectangle.to_dictionary(), expected_dict)


class TestRectangleUpdate(unittest.TestCase):

    def test_update_args(self):
        rectangle = MyRectangle(5, 10, 2, 3, 4)
        rectangle.update(1, 6, 1, 1, 1)
        self.assertEqual(rectangle.width, 6)
        self.assertEqual(rectangle.height, 1)   
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 1)

    def test_update_kwargs(self):
        rectangle = MyRectangle(5, 10, 2, 3, 4)
        rectangle.update(width=8, height=6, x=1, y=1, id=7)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 1)
        self.assertEqual(rectangle.id, 7)

    def test_update_args_and_kwargs(self):
        rectangle = MyRectangle(5, 10, 2, 3, 4)
        rectangle.update(width=8, height=6, id=7)
        self.assertEqual(rectangle.width, 8)
        self.assertEqual(rectangle.height, 6)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 7)
        
class TestRectangleStrDisplay(unittest.TestCase):
    
    def test_str_method_one_arg(self):
        r = MyRectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)
