import json

from django.core.urlresolvers import reverse

from common.utils import get_random_name
from common.tests import BaseTestCase
from library.tests import create_library
from sample.tests import create_sample

from request.models import Request
from index_generator.tests import create_pool
from .models import Pooling


def create_pooling_object(user, add_library=False, add_sample=False,
                          sample_failed=False):
    library = None
    sample = None

    if add_library:
        library = create_library(get_random_name(), 2)

    if add_sample:
        sample = create_sample(get_random_name(), 2)

    pool = create_pool(user)

    request = Request(user=user)
    request.save()

    if library:
        request.libraries.add(library)
        pool.libraries.add(library)
        pooling_object = Pooling.objects.get(library=library)

    if sample:
        request.samples.add(sample)
        pool.samples.add(sample)

        # Update the sample instance because after being added to the pool,
        # it was modified
        sample = sample.__class__.objects.get(pk=sample.pk)

        if sample_failed:
            sample.status = -1  # failed quality check
            sample.save()
            pooling_object = sample

        else:
            sample.status = 3  # passed quality check
            sample.save()
            pooling_object = Pooling.objects.get(sample=sample)

    return pooling_object


# Models

class TestPoolingModel(BaseTestCase):

    def setUp(self):
        self.user = self._create_user('test@test.io', 'foo-bar')
        self.pooling_obj = create_pooling_object(self.user, add_library=True)

    def test_name(self):
        self.assertTrue(isinstance(self.pooling_obj, Pooling))
        self.assertEqual(self.pooling_obj.__str__(), '{} ({})'.format(
            self.pooling_obj.library.name,
            self.pooling_obj.library.barcode,
        ))

    def test_create_pooling_object_from_library(self):
        """
        Ensure a Pooling object is created when a library is added to a pool.
        """
        library = create_library(get_random_name())
        pool = create_pool(self.user)
        pool.libraries.add(library)
        self.assertEqual(Pooling.objects.filter(library=library).count(), 1)

    def test_create_pooling_object_from_sample(self):
        """
        Ensure a Pooling object is created when a sample passed the quality
        check (and gets the status 4) after the Library Preparation step.
        """
        sample = create_sample(get_random_name(), status=3)
        pool = create_pool(self.user)
        pool.samples.add(sample)

        # Update the sample instance because after being added to the pool,
        # it was modified
        sample = sample.__class__.objects.get(pk=sample.pk)

        sample.status = 3  # passed quality check
        sample.save()

        self.assertEqual(Pooling.objects.filter(sample=sample).count(), 1)


# Views

class TestPooling(BaseTestCase):

    def setUp(self):
        self.user = self._create_user('test@test.io', 'foo-bar')

    def test_pooling_list(self):
        """ Ensure get pooling list behaves correctly. """
        self.client.login(email='test@test.io', password='foo-bar')

        pooling_object1 = create_pooling_object(self.user, add_library=True)
        pooling_object2 = create_pooling_object(self.user, add_sample=True)

        # Create failed sample
        failed_sample = create_pooling_object(self.user, add_sample=True,
                                              sample_failed=True)

        response = self.client.get(reverse('pooling-list'))
        data = response.json()
        objects = [x['name'] for x in data]

        self.assertEqual(response.status_code, 200)
        self.assertIn(pooling_object1.library.name, objects)
        self.assertIn(pooling_object2.sample.name, objects)
        self.assertNotIn(failed_sample.name, objects)

    def test_pooling_list_non_staff(self):
        """Ensure error is thrown if a non-staff user tries to get the list."""
        self._create_user('non-staff@test.io', 'test', False)
        self.client.login(email='non-staff@test.io', password='test')
        response = self.client.get(reverse('pooling-list'))
        self.assertTrue(response.status_code, 403)

    def test_update_pooling_object(self):
        """ Ensure update pooling object behaves correctly. """
        self.client.login(email='test@test.io', password='foo-bar')
        pooling_object = create_pooling_object(self.user, add_library=True)

        response = self.client.post(reverse('pooling-edit'), {
            'data': json.dumps([{
                'pk': pooling_object.library.pk,
                'record_type': 'Library',
                'concentration_c1': 1.0,
            }])
        })

        updated_obj = Pooling.objects.get(library=pooling_object.library)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])
        self.assertEqual(updated_obj.concentration_c1, 1.0)

    def test_contains_invalid_objects(self):
        """
        Ensure update pooling objects containing invalid objects
        behaves correctly.
        """
        self.client.login(email='test@test.io', password='foo-bar')

        pooling_object1 = create_pooling_object(self.user, add_library=True)
        pooling_object2 = create_pooling_object(self.user, add_sample=True)

        response = self.client.post(reverse('pooling-edit'), {
            'data': json.dumps([{
                'pk': pooling_object1.library.pk,
                'record_type': 'Library',
                'concentration_c1': 1.0,
            }, {
                'pk': pooling_object2.sample.pk,
                'record_type': 'Sample',
                'concentration_c1': 'blah',
            }])
        })
        data = response.json()
        updated_obj = Pooling.objects.get(library=pooling_object1.library)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Some records cannot be updated.')
        self.assertEqual(updated_obj.concentration_c1, 1.0)

    def test_update_invalid_pooling_object(self):
        """ Ensure update invalid pooling object behaves correctly. """
        self.client.login(email='test@test.io', password='foo-bar')
        pooling_object = create_pooling_object(self.user, add_library=True)

        response = self.client.post(reverse('pooling-edit'), {
            'data': json.dumps([{
                'pk': pooling_object.library.pk,
                'record_type': 'Library',
                'concentration_c1': 'blah',
            }])
        })

        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Invalid payload.')

    def test_contains_invalid_id(self):
        """
        Ensure update library pooling object containing objects with
        invalid ids bahaves correctly.
        """
        self.client.login(email='test@test.io', password='foo-bar')
        pooling_object = create_pooling_object(self.user, add_library=True)

        response = self.client.post(reverse('pooling-edit'), {
            'data': json.dumps([{
                'pk': 'blah',
                'record_type': 'Sample',
                'concentration_c1': 1.0,
            }, {
                'pk': pooling_object.library.pk,
                'record_type': 'Library',
                'concentration_c1': 2.0,
            }])
        })

        updated_obj = Pooling.objects.get(library=pooling_object.library)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])
        self.assertEqual(updated_obj.concentration_c1, 2.0)

    def test_quality_check_passed(self):
        """ Ensure quality check has passed behaves correctly. """
        self.client.login(email='test@test.io', password='foo-bar')
        pooling_object = create_pooling_object(self.user, add_library=True)

        response = self.client.post(reverse('pooling-edit'), {
            'data': json.dumps([{
                'pk': pooling_object.library.pk,
                'record_type': 'Library',
                'quality_check': 'passed',
            }])
        })

        updated_obj = Pooling.objects.get(library=pooling_object.library)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])
        self.assertEqual(updated_obj.library.status, 4)

    def test_quality_check_failed(self):
        """ Ensure quality check has failed behaves correctly. """
        self.client.login(email='test@test.io', password='foo-bar')
        pooling_object = create_pooling_object(self.user, add_sample=True)

        response = self.client.post(reverse('pooling-edit'), {
            'data': json.dumps([{
                'pk': pooling_object.sample.pk,
                'record_type': 'Sample',
                'quality_check': 'failed',
            }])
        })

        updated_obj = Pooling.objects.get(sample=pooling_object.sample)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['success'])
        self.assertEqual(updated_obj.sample.status, -1)

    def test_invalid_json(self):
        """ Ensure error is thrown if the JSON object is empty. """
        self.client.login(email='test@test.io', password='foo-bar')
        response = self.client.post(reverse('pooling-edit'), {})
        data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertFalse(data['success'])
        self.assertIn('Invalid payload.', data['message'])
