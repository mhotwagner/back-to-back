from django.db import IntegrityError
from django.test import TestCase

# Create your tests here.
from .models import Calculation


class TestCalculation(TestCase):
    def test_id_is_a_required_param(self):
        with(self.assertRaises(IntegrityError)):
            Calculation.objects.create()

    def test_it_can_be_created_with_an_id(self):
        Calculation.objects.create(id=1)
        calculation = Calculation.objects.get(id=1)
        self.assertEqual(calculation.id, 1)
