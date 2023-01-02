import requests

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from facial.serializers import AuthenticationSerializer

from . import models


CONTROL_ID_URL = 'http://10.8.4.6/'
CONTROL_ID_URL_LOGIN = CONTROL_ID_URL + 'login.fcgi'
CONTROL_ID_URL_DOOR = CONTROL_ID_URL + 'execute_actions.fcgi?session='
CONTROL_ID_URL_OPEN_DOOR = CONTROL_ID_URL + 'open_door'


def authenticate():

    auth = models.Authentication.objects.filter(is_active=True).first()

    login_data = {
        "login": auth.username,
        "password": auth.password
    }

    open_door_data = {
        "actions": [
            {
                "action": "sec_box",
                "parameters": "id=65793,reason=3,timeout=10000"
            }
        ]
    }

    login = requests.post(CONTROL_ID_URL_LOGIN, data=login_data)

    if login.ok:
        session_id = login.json().get('session')
    else:
        raise ValueError(f'Login attempt error: {login.json()}')

    open = requests.post(CONTROL_ID_URL_DOOR +
                         session_id, json=open_door_data)

    if open.ok:
        print('open_door_data: ok')
    else:
        raise ValueError(f'Login attempt error: {open.json(), open.url}')


# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         authenticate()
#         return Response({})


@api_view(http_method_names=['GET', 'POST'])
def door_test(request):
    """

    """
    authenticate = models.Authentication.objects.filter(is_active=True)
    serializer = AuthenticationSerializer(
        instance=authenticate,
        many=True,
        context={'request': request},
    )
    return Response(serializer.data)
