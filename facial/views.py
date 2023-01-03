import requests
import os

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import response, status, views
from django.conf import settings

from facial.serializers import DataRequestSerializer

from . import models


def authenticate():
    """_summary_

    Raises:
        ValueError: _description_
        ValueError: _description_
    """

    auth = models.Authentication.objects.filter(is_active=True).first()

    login_data = {
        "login": auth.username,
        "password": auth.password
    }

    open_door_data = {
        "actions": [
            {
                "action": "sec_box",
                "parameters": "id=65793,reason=3,timeout=5000"
            }
        ]
    }

    # import pdb
    # pdb.set_trace()
    login = requests.post(settings.CONTROL_ID_URL_LOGIN, data=login_data)

    if login.ok:
        session_id = login.json().get('session')
    else:
        raise ValueError(f'Login attempt error: {login.json()}')

    import pdb
    pdb.set_trace()
    open = requests.post(
        f'{settings.CONTROL_ID_URL_DOOR}{session_id}',
        json=open_door_data)

    if open.ok:
        print(f'\n{settings.CONTROL_ID_URL_DOOR}{session_id}\n')
    else:
        raise ValueError(f'Login attempt error: {open.json(), open.url}')


class OpenDoor(views.APIView):

    """


    Args:
        request (dict): Uses a data response list.

    Returns:
        queryset (JSON): return list of data FindFace.
    """

    def post(self, request):

        authenticate()
        serializer = DataRequestSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
