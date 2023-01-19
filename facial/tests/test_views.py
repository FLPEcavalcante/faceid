from django.test import TestCase
from django.urls import reverse

from rest_framework import status

from . import recipes


class TestOpenDoorView(TestCase):
    """Test open door view class."""

    def setUp(self):
        """Set up data for tests, created user with token."""

        self.recipes = recipes.DataRequestRecipes()
        self.user = self.recipes.user.make()

        self.data_request = self.recipes.data_request.make(id=1)
        self.url = reverse('facial:open-door')

    def test_request_data_creation_data_with_error(self):
        """Method to test input data with error on view."""

        data = [
            {
                "id": "4491920800946233265",
                "thumbnail": "https://findface.hex.hex360/uploads/2023/01/10/face_event/141458_face_thumbnail_5qR3lj.jpg",
                "fullframe": "https://findface.hex.hex360/uploads/2023/01/10/face_event/141458_face_full_frame_hjeyep.jpg",
                "matched": "True",
                "created_date": "2023-01-10T 00:00:00",
                "facial_creation_date": "2023-01-10T 00:00:00"
            }
        ]

        response = self.client.post(self.url)
        self.assertTrue(status.is_client_error(response.status_code))

        response = self.client.post(self.url, data=data)
        self.assertTrue(status.is_client_error(response.status_code))
