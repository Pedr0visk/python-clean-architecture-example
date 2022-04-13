import unittest
from datetime import datetime as dt
from dataclasses import is_dataclass
from category.domain.entities import Category


class TestCategoryUnit(unittest.TestCase):
    def test_is_dataclass_instance(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        c = Category(name="Movie")

        self.assertEqual(c.name, "Movie")
        self.assertEqual(c.description, None)
        self.assertEqual(c.is_active, True)
        self.assertIsInstance(c.created_at, dt)

        now = dt.now()

        c = Category(
            name="Movie", 
            description="some description", 
            is_active=True, 
            created_at=now
        )

        self.assertEqual(c.name, "Movie")
        self.assertEqual(c.description, "some description")
        self.assertEqual(c.is_active, True)
        self.assertEqual(c.created_at, now)
        self.assertIsInstance(c.created_at, dt)

    def test_if_created_at_is_generated_in_constructor(self):
        c1 = Category(name="Movie 1")
        c2 = Category(name="Movie 2")

        self.assertNotEqual(
            c1.created_at.timestamp(),
            c2.created_at.timestamp(),
        )