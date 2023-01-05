import requests

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import response, status, views
from django.conf import settings

from facial.control_id.views import OpenDoorRequest
from facial.serializers import DataRequestSerializer

from . import models


# def authenticate():
#     """Method for validated authencication of login the user.

#     Args:
#         login_data(JSON):

#     Return:
#         value (session): return a value for session validated.
#     """

#     auth = models.Authentication.objects.filter(is_active=True).first()

#     login_data = {
#         "login": auth.username,
#         "password": auth.password
#     }

#     open_door_data = {
#         "actions": [
#             {
#                 "action": "sec_box",
#                 "parameters": "id=65793,reason=3,timeout=5000"
#             }
#         ]
#     }

#     login = requests.post(settings.CONTROL_ID_URL_LOGIN, data=login_data)

#     if login.ok:
#         session_id = login.json().get('session')
#     else:
#         raise ValueError(f'Login attempt error: {login.json()}')

#     open = requests.post(
#         f'{settings.CONTROL_ID_URL_DOOR}{session_id}',
#         json=open_door_data)

#     if open.ok:
#         print(f'\n{settings.CONTROL_ID_URL_DOOR}{session_id}\n')
#     else:
#         raise ValueError(f'Login attempt error: {open.json(), open.url}')


class OpenDoor(views.APIView):

    """Method Class for open door action.

    Args:
        request (dict): Uses a data response list.

    Returns:
        queryset (JSON): return list of data FindFace.
    """

    def post(self, request):

        OpenDoorRequest()
        # authenticate()
        serializer = DataRequestSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
