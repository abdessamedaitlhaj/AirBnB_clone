#!/usr/bin/python3
"""Module that defines unittest for Place class"""

from models.place import Place
from models.base_model import BaseModel
import models
import unittest
import datetime as dt


class TestPlace(unittest.TestCase):
    """Desfines testcases for Place class"""

    def test_creation(self):
        """Create an instance of Place class"""
        p = Place()
        p.name = "halimon"
        p.description = "great place"
        p.number_rooms = 10
        p.number_bathrooms = 3
        p.max_guest = 100
        p.price_by_night = 120

        self.assertTrue(p.name, "halimon")
        self.assertTrue(p.description, "great place")
        self.assertTrue(p.number_rooms, 10)
        self.assertTrue(p.number_bathrooms, 3)
        self.assertTrue(p.max_guest, 100)
        self.assertTrue(p.price_by_night, 120)
        self.assertIsInstance(p, Place)
        self.assertTrue(issubclass(Place, BaseModel))

    def test_to_dict(self):
        """Test cases for to_dict method"""
        p = Place()
        p.name = "halimon"
        p.description = "great place"
        p.number_rooms = 10
        expected_result = [
                'id',
                'created_at',
                'updated_at',
                'name',
                'description',
                'number_rooms',
                '__class__'
                ]
        self.assertEqual(expected_result, list(p.to_dict().keys()))

    def test_save(self):
        """Test cases for save method"""
        p = Place()
        p.created_at = p.updated_at = dt.datetime.now()
        self.assertEqual(p.created_at, p.updated_at)
        p.save()
        self.assertNotEqual(p.created_at, p.updated_at)
        key = 'Place.' + p.id
        all_objects = models.storage.all()
        self.assertIn(key, all_objects.keys())


if __name__ == "__main__":
    unittest.main()
