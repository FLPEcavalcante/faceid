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

    # def test_data_request_creation_data_with_error(self):
    #     """Method to test input data with error on view."""

    #     result = [
    #         {
    #             'id': '4491687902580142398',
    #             'thumbnail': 'https://findface.hex.hex360/uploads/2023/01/09/face_event/140856_face_thumbnail_NgLm3g.jpg',
    #             'fullframe': 'https://findface.hex.hex360/uploads/2023/01/09/face_event/140856_face_full_frame_XaROsL.jpg',
    #             'matched': 'True',
    #             'created_date': '2023-01-09T00:00:00',
    #             'facial_creation_date': '2023-01-09T00:00:00',
    #         }
    #     ]

    #     client = OpenDoorView()

    #     response = client.post(self.url, data={}, format='json')
    #     self.assertTrue(status.is_client_error(response.status_code))

    #     response = client.post(self.url, data=result, format='json')
    #     self.assertTrue(status.is_client_error(response.status_code))

    def test_drone_path_lits_view_with_success(self):
        """Method to test drone list route with success status code."""

        import pdb
        pdb.set_trace()
        url = reverse('facial/open-door/')

        client = self.data_request()
        response = client.get(url, format='json')

        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(len(response.data), 1)
