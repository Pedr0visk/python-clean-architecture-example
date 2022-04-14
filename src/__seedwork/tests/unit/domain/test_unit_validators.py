import unittest

from __seedwork.domain.validators import ValidatorRules


class TestValidatorsRulesUnit(unittest.TestCase):
    def test_values_method(self):
        validator = ValidatorRules.values("some value", "prop")
        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, "some value")
        self.assertEqual(validator.prop, "prop")

    def test_required_rule(self):
        pass
