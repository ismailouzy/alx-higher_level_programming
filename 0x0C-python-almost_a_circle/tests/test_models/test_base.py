#!/usr/bin/python3
"""Unittests for base.py.

"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class MyTestBaseInstantiation(unittest.TestCase):
    """Unittests
    ."""

    def testDefaultID(self):
        base_one = Base()
        base_two = Base()
        self.assertEqual(base_one.id, base_two.id - 1)

    def testUniqueID(self):
        self.assertEqual(12, Base(12).id)

    def testNoneID(self):
        base_one = Base(None)
        base_two = Base(None)
        self.assertEqual(base_one.id, base_two.id - 1)

    def testMultipleBases(self):
        base_one = Base()
        base_two = Base()
        base_three = Base()
        self.assertEqual(base_one.id, base_three.id - 2)

    def testIDPublic(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def testNbInstancesPrivate(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def testMultipleTypesOfID(self):
        id_values = ["hello", 5.5, complex(5), {"a": 1, "b": 2},
                     True, [1, 2, 3], (1, 2), {1, 2, 3},
                     frozenset({1, 2, 3}), range(5), b'Python',
                     bytearray(b'abcefg'), memoryview(b'abcefg'),
                     float('inf')]

        for value in id_values:
            with self.subTest(value=value):
                base_instance = Base(value)
                self.assertEqual(base_instance.id, value)

    def testNbInstancesAfterUniqueID(self):
        base_one = Base()
        base_two = Base(12)
        base_three = Base()
        self.assertEqual(base_one.id, base_three.id - 1)

    def testTwoArgs(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class MyTestBaseToJsonString(unittest.TestCase):
    """Unittests
    ."""

    def testSquareDictToJsonString(self):
        s = Square(5, 2, 3, 7)
        json_str = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(str, type(json_str))
        self.assertTrue(len(json_str) > 0)

    def testRectangleDictsToJsonString(self):
        r1 = Rectangle(4, 6, 2, 1, 8)
        r2 = Rectangle(3, 5, 1, 2, 10)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(str, type(json_str))
        self.assertTrue(len(json_str) > 0)

    def testEmptyListToJsonString(self):
        json_str = Base.to_json_string([])
        self.assertEqual("[]", json_str)

    def testNoneToJsonString(self):
        json_str = Base.to_json_string(None)
        self.assertEqual("[]", json_str)

    def testNoArgsToJsonString(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def testMoreThanOneArgToJsonString(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class MyTestBaseSaveToFile(unittest.TestCase):
    """Unittests
    ."""

    def testSaveSquareToFile(self):
        s = Square(5, 2, 3, 7)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def testSaveRectanglesToFile(self):
        r1 = Rectangle(4, 6, 2, 1, 8)
        r2 = Rectangle(3, 5, 1, 2, 10)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def testSaveEmptyListToFile(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def testSaveNoArgsToFile(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def testSaveMoreThanOneArgToFile(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 1)


class MyTestBaseFromJsonString(unittest.TestCase):
    """Unittests
    ."""

    def testFromJsonStringSquareType(self):
        s = Square(8, 2, 3, 4)
        Square.save_to_file([s])
        json_str = Base.to_json_string([s.to_dictionary()])
        output = Square.from_json_string(json_str)
        self.assertEqual(type(output), list)

    def testFromJsonStringRectanglesType(self):
        r1 = Rectangle(4, 6, 2, 1, 8)
        r2 = Rectangle(3, 5, 1, 2, 10)
        Rectangle.save_to_file([r1, r2])
        json_str = Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()])
        output = Rectangle.from_json_string(json_str)
        self.assertEqual(type(output), list)

    def testFromJsonStringEmptyList(self):
        output = Base.from_json_string("[]")
        self.assertEqual([], output)

    def testFromJsonStringNone(self):
        output = Base.from_json_string(None)
        self.assertEqual([], output)

    def testFromJsonStringNoArgs(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def testFromJsonStringMoreThanOneArg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class MyTestBaseCreate(unittest.TestCase):
    """Unittests
    ."""

    def testCreateSquareOriginal(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def testCreateSquareNew(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def testCreateSquareIs(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def testCreateSquareEquals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)
