
import factory

from django.db import IntegrityError
from django.test import TestCase

from .models import Calculation


class CalculationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Calculation


class TestCalculationModel(TestCase):
    def test_id_is_a_required_param(self):
        with(self.assertRaises(IntegrityError)):
            CalculationFactory.create()

    def test_it_can_be_created_with_an_id(self):
        CalculationFactory.create(id=1)
        calculation = Calculation.objects.get(id=1)
        self.assertEqual(calculation.id, 1)

    def test_number_is_same_as_id(self):
        calculation = CalculationFactory.create(id=1)
        self.assertEqual(calculation.number, calculation.id)

    def test_occurrences_defaults_to_0(self):
        calculation = CalculationFactory.create(id=1)
        self.assertEqual(calculation._occurrences, 0)

    def test_occurrences_property_returns_occurrences_value(self):
        calculation = CalculationFactory.create(id=1)
        self.assertEqual(calculation.occurrences, 0)

    def test_occurrences_does_not_have_a_setter(self):
        calculation = CalculationFactory.create(id=1)
        with(self.assertRaises(AttributeError)):
            calculation.occurrences = 0

    def test_increment_occurrences_increments_occurrences(self): # duh
        calculation = CalculationFactory.create(id=1)
        self.assertEqual(calculation.occurrences, 0)
        calculation.increment_occurrences()
        calculation.save()
        fetched_calculation = Calculation.objects.get(id=1)
        self.assertEqual(fetched_calculation.occurrences, 1)

    def test_last_occurrence_is_set_when_model_is_created(self):
        calculation = CalculationFactory.create(id=1)
        self.assertTrue(calculation.last_occurrence)

    def test_value_returns_difference_between_sum_of_squares_and_square_of_sums_for_sequence(self):
        calculation = CalculationFactory.create(id=3)
        # 3^2 + 2^2 + 1^2 = 14
        # (3 + 2 + 1)^2 = 36
        # 14 - 36 = -22
        self.assertEqual(calculation.value, 22)
