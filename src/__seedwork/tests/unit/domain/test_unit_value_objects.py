
from abc import ABC
import unittest
import uuid 

from dataclasses import FrozenInstanceError, dataclass, is_dataclass
from unittest.mock import patch
from __seedwork.domain import value_objects
from __seedwork.domain.value_objects import UniqueEntityID, ValueObject
from __seedwork.domain.exceptions import InvalidUUIDException


@dataclass(frozen=True)
class StubOneProp(ValueObject):
    prop: str

@dataclass(frozen=True)
class StubTwoProp(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_is_dataclass_instance(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_is_abc_instance(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_init_prop(self):
        vo1 = StubOneProp(prop="value")
        self.assertEqual(vo1.prop, "value")

        vo2 = StubTwoProp(prop1="value1", prop2="value2")
        self.assertEqual(vo2.prop1, "value1")
        self.assertEqual(vo2.prop2, "value2")

    def test_convert_to_string(self):
        vo1 = StubOneProp(prop="value")
        self.assertEqual(vo1.prop, str(vo1))

        vo2 = StubTwoProp(prop1="value1", prop2="value2")
        self.assertEqual('{"prop1": "value1", "prop2": "value2"}', str(vo2))

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = StubOneProp(prop="value")
            value_object.prop = "prop1"

class TestValueObjectsUnit(unittest.TestCase):

    def test_is_dataclass_instance(self):
        self.assertTrue(is_dataclass(UniqueEntityID))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityID,
            "_UniqueEntityID__validate",
            autospec=True,
            side_effect=UniqueEntityID._UniqueEntityID__validate
        ) as mock_validate:

            with self.assertRaises(InvalidUUIDException) as assert_error:
                UniqueEntityID("fake id")

                mock_validate.assert_called_once()
                self.assertEqual(assert_error.exception.args[0], "ID must be a valid UUID")
    
    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityID,
            "_UniqueEntityID__validate",
            autospec=True,
            side_effect=UniqueEntityID._UniqueEntityID__validate
        ) as mock_validate:
            value_object = UniqueEntityID("0bd8fd62-244b-43fd-998e-786c3a187bfe")
            mock_validate.assert_called_once()
            self.assertEqual(value_object.id, "0bd8fd62-244b-43fd-998e-786c3a187bfe")

        uuid_value = uuid.uuid4()
        value_object = UniqueEntityID(uuid_value)
        self.assertEqual(value_object.id, str(uuid_value))

    def test_generate_id_when_no_passed_id_in_constructor(self):
        with patch.object(
            UniqueEntityID,
            "_UniqueEntityID__validate",
            autospec=True,
            side_effect=UniqueEntityID._UniqueEntityID__validate
        ) as mock_validate:
            value_object = UniqueEntityID()
            uuid.UUID(value_object.id)
            mock_validate.assert_called_once()

    def test_is_immutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityID()
            value_object.id = "fake id"

    def test_convert_to_str(self):
        value_object = UniqueEntityID()
        self.assertEqual(value_object.id, str(value_object))