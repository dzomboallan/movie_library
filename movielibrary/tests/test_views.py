from inspect import classify_class_attrs
from django.test import TestCase
from django.urls import reverse
from movielibrary.models import Actor

class ActorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 actors pagination tests
        number_of_actors = 13

        for actor_id in range(number_of_actors):
            Actor.objects.create(first_name=f'Christian{actor_id}',
                                 last_name=f'Surname{actor_id}',
                                 )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/movielibrary/actor/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('actor'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('actor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movielibrary/actor_list.html')

    def test_pagination_is_ten(self):
        response = self.client.get(reverse('actor'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['actor_list']), 10)

    def test_lists_all_actors(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get(reverse('actor')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['actor_list']), 3)

