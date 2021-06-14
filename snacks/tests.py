from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class snacks_tests(TestCase):
    def test_snack_list(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response, 'snack_list.html')
