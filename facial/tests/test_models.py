from django.test import TestCase

from facial import models

from . import recipes


class TestDataRequest(TestCase):
    """Model test class to check request data."""

    def setUp(self):
        """Set up data for tests."""

        self.recipes = recipes.DataRequestRecipes()
        self.data_request = self.recipes.data_request.make()
        import pdb
        pdb.set_trace()

    def test_user_settings_invalid_data_creation(self):
        """Test user settings invalid creation without user."""
        with self.assertRaises(Exception):
            self.recipes.user.make(
                user=None
            )

    def test_data_request_creation(self):
        """Test data request check creation."""

        self.assertTrue(models.DataRequest.objects.count())

    def test_data_request_type_str(self):
        """"Test data request type str."""

        self.assertIsInstance(
            recipes.User.objects.first().__str__(), str)

    def test_data_request_create_multiple(self):
        """Test verification data request."""

        for i in range(10):
            self.data_request = self.recipes.data_request.make(
                id=f'{i}',
                thumbnail=f'{i}',
                fullframe=f'{i}',
            )

        self.assertTrue(models.DataRequest.objects.count() > 10)

    def test_data_request_post_save(self):
        """Test get and access to field of data request."""

        data = models.DataRequest.objects.first()
        self.assertTrue(data.id)
