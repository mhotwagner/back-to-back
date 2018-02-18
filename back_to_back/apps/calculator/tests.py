
import factory

from django.db import IntegrityError
from django.test import TestCase

# Create your tests here.
from .models import Calculation


class CalculationFactory(factory.DjangoModelFactory):
    class Meta:
        model = Calculation


class TestCalculation(TestCase):
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

    
