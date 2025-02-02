from django.test import TestCase
from .models import FAQ


class FAQTests(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="What is Django?", answer="Django is a web framework.")
        self.assertEqual(faq.question, "What is Django?")
