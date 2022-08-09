from django.test import TestCase
from movielibrary.models import Actor

# Create your tests here.
class ActorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set uo non-modified objects used by all test methods.
        Actor.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        actor = Actor.objects.get(id=1)
        field_label = actor._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        actor = Actor.objects.get(id=1)
        max_length = actor._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        actor = Actor.objects.get(id=1)
        expected_object_name = f'{actor.last_name},{actor.first_name}'
        self.assertEqual(str(actor), expected_object_name)

    def test_get_absolute_url(self):
        actor = Actor.objects.get(id=1)
        # This will also fail if urlconf is not defined.
        self.assertEqual(actor.get_absolute_url(), '/movielibrary/actor/1')