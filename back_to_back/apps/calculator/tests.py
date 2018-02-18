
import factory

from django.db import IntegrityError
from django.test import TestCase, Client
from django.urls import reverse

from .serializers import CalculationSerializer
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


class TestCalculationSerializer(TestCase):
    def test_it_returns_data(self):
        calculation = CalculationFactory.create(id=3)
        calculation_serializer = CalculationSerializer(calculation)

        data = calculation_serializer.data

        self.assertIsNotNone(data['datetime'])
        self.assertEqual(data['number'], 3)
        self.assertEqual(data['value'], 22)
        self.assertEqual(data['occurrences'], 0)
        self.assertIsNotNone(data['last_occurrence'])


class TestCalculationView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_it_returns_a_400_if_no_query_parameter_is_provided(self):
        response = self.client.get(reverse('calculator:calculation'))
        self.assertEqual(response.status_code, 400)

    def test_it_returns_400_if_number_is_not_a_number(self):
        response = self.client.get('{}?number=notanumber'.format(reverse('calculator:calculation')))
        self.assertEqual(response.status_code, 400)

    def test_it_returns_400_if_number_is_less_than_1(self):
        response = self.client.get('{}?number=-1'.format(reverse('calculator:calculation')))
        self.assertEqual(response.status_code, 400)

    def test_it_returns_400_if_number_is_greater_than_100(self):
        response = self.client.get('{}?number=101'.format(reverse('calculator:calculation')))
        self.assertEqual(response.status_code, 400)

    def test_it_returns_200_when_number_param_refers_to_an_existing_solution(self):
        CalculationFactory.create(id=10)
        response = self.client.get('{}?number=10'.format(reverse('calculator:calculation')))
        self.assertEqual(response.status_code, 200)

    def test_it_returns_200_when_number_param_refers_to_a_not_yet_existing_solution(self):
        response = self.client.get('{}?number=10'.format(reverse('calculator:calculation')))
        self.assertEqual(response.status_code, 200)

    def test_it_returns_a_serialized_solution_for_a_valid_number(self):
        response = self.client.get('{}?number=10'.format(reverse('calculator:calculation')))

        self.assertIsNotNone(response.data)

        self.assertIsNotNone(response.data.get('datetime'))
        self.assertEqual(response.data.get('value'), 2640)
        self.assertEqual(response.data.get('number'), 10)
        self.assertEqual(response.data.get('occurrences'), 0)
        self.assertIsNone(response.data.get('last_datetime'))

    def test_making_a_valid_query_increments_the_occurrences_count_for_that_solution(self):
        first_response = self.client.get('{}?number=10'.format(reverse('calculator:calculation')))

        self.assertEqual(first_response.data.get('occurrences'), 0)

        second_response = self.client.get('{}?number=10'.format(reverse('calculator:calculation')))

        self.assertEqual(second_response.data.get('occurrences'), 1)

    def test_making_a_valid_query_updates_last_occurrence_for_that_solution(self):
        first_response = self.client.get('{}?number=10'.format(reverse('calculator:calculation')))

        second_response = self.client.get('{}?number=10'.format(reverse('calculator:calculation')))

        self.assertNotEqual(
            first_response.data.get('last_occurrence'),
            second_response.data.get('last_occurrence'),
        )
