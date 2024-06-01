from django.test import TestCase
from rest_framework.test import APIClient
from .models import Part
from .utils import most_common_words


class PartTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.part = Part.objects.create(
            name='Test Part',
            sku='TEST123',
            description='A test part',
            weight_ounces=10,
            is_active=True
        )

    def test_create_part(self):
        response = self.client.post('/api/parts/', {
            'name': 'New Part',
            'sku': 'NEW123',
            'description': 'A new part',
            'weight_ounces': 20,
            'is_active': True
        })
        self.assertEqual(response.status_code, 201)

    def test_get_parts(self):
        response = self.client.get('/api/parts/')
        self.assertEqual(response.status_code, 200)

    def test_update_part(self):
        response = self.client.put(f'/api/parts/{self.part.id}/', {
            'name': 'Updated Part',
            'sku': 'UPDATED123',
            'description': 'An updated part',
            'weight_ounces': 30,
            'is_active': False
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'Updated Part')

    def test_delete_part(self):
        response = self.client.delete(f'/api/parts/{self.part.id}/')
        self.assertEqual(response.status_code, 204)


class UtilsTests(TestCase):
    def test_returns_most_common_words(self):
        descriptions = ["apple banana", "banana orange", "apple orange", "apple banana orange"]
        expected_result = [{'word': 'apple', 'count': 3}, {'word': 'banana', 'count': 3}, {'word': 'orange', 'count': 3}]
        self.assertEqual(most_common_words(descriptions), expected_result)

    def test_returns_empty_list_when_no_descriptions(self):
        descriptions = []
        expected_result = []
        self.assertEqual(most_common_words(descriptions), expected_result)

    def test_returns_correct_count_when_single_word_descriptions(self):
        descriptions = ["apple", "apple", "banana"]
        expected_result = [{'word': 'apple', 'count': 2}, {'word': 'banana', 'count': 1}]
        self.assertEqual(most_common_words(descriptions), expected_result)

    def test_returns_correct_count_when_descriptions_have_multiple_same_words(self):
        descriptions = ["apple apple", "banana banana banana", "orange"]
        expected_result = [{'word': 'banana', 'count': 3}, {'word': 'apple', 'count': 2}, {'word': 'orange', 'count': 1}]
        self.assertEqual(most_common_words(descriptions), expected_result)