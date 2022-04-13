import unittest
from abc import ABC
from dataclasses import dataclass, is_dataclass
from __seedwork.domain.entities import Entity
from __seedwork.domain.value_objects import UniqueEntityID


@dataclass(frozen=True, kw_only=True, slots=True)
class StubEntity(Entity):
    prop1: str
    prop2: str


class TestEntityUnit(unittest.TestCase):
    def test_is_dataclass_instance(self):
        self.assertTrue(is_dataclass(Entity))

    def test_is_abc_instance(self):
        self.assertIsInstance(Entity(), ABC)

    def test_set_id_and_props(self):
        entity = StubEntity(prop1="value1", prop2="value2")
        self.assertEqual(entity.prop1, "value1")
        self.assertEqual(entity.prop2, "value2")
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityID)
        self.assertEqual(entity.unique_entity_id.id, entity.id)

    def test_accept_a_valid_uuid(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityID(
                "d6a4d428-ccb3-4a80-96c7-31e655a2d02b"),
            prop1="value1",
            prop2="value2",
        )

        self.assertEqual(entity.id, "d6a4d428-ccb3-4a80-96c7-31e655a2d02b")

    def test_to_dict_method(self):
        entity = StubEntity(
            unique_entity_id=UniqueEntityID(
                "d6a4d428-ccb3-4a80-96c7-31e655a2d02b"),
            prop1="value1",
            prop2="value2",
        )

        self.assertDictEqual(entity.to_dict(), {
            "id": "d6a4d428-ccb3-4a80-96c7-31e655a2d02b",
            "prop1": "value1",
            "prop2": "value2",
        })

    def test_set_method(self):
        entity = StubEntity(prop1="value1", prop2="value2")
        entity._set("prop1", "changed")
        self.assertEqual(entity.prop1, "changed")
