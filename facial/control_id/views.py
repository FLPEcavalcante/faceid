from django.conf import settings
import requests
from facial import models, views


class OpenDoorRequest():

    def __init__(self, login_data, open_door_data):
        self.login_data = login_data
        self.open_door_data = open_door_data

    auth = models.Authentication.objects.filter(is_active=True).first()

    log = OpenDoorRequest(
        login_data={
            "login": auth.username,
            "password": auth.password
        }
    )
    print(log.login_data)

    door = OpenDoorRequest(
        open_door_data={
            "actions": [
                {
                    "action": "sec_box",
                    "parameters": "id=65793,reason=3,timeout=5000"
                }
            ]
        }
    )
    print(door.open_door_data)

    def authenticate(self):
        """Method for validated authencication of login the user.

        Args:
            login_data(JSON):

        Return:
            value (session): return a value for session validated.
        """

        login = requests.post(
            settings.CONTROL_ID_URL_LOGIN, self.log
        )

        if login.ok:
            session_id = login.json().get('session')
        else:
            raise ValueError(f'Login attempt error: {login.json()}')

        open = requests.post(
            f'{settings.CONTROL_ID_URL_DOOR}{session_id}', self.door
        )

        if open.ok:
            print(f'\n{settings.CONTROL_ID_URL_DOOR}{session_id}\n')
        else:
            raise ValueError(f'Login attempt error: {open.json(), open.url}')
