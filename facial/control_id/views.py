from django.conf import settings
import requests
from facial import models, views


# class OpenDoorRequest:
def authenticate():
    """Method for validated authencication of login the user.

        Args:
            login_data(JSON):

        Return:
            value (session): return a value for session validated.
        """

    auth = models.Authentication.objects.filter(is_active=True).first()

    login_data = {
        "login": auth.username,
        "password": auth.password
    }
    import pdb
    pdb.set_trace()
    open_door_data = {
        "actions": [
            {
                "action": "sec_box",
                "parameters": "id=65793,reason=3,timeout=5000"
            }
        ]
    }

    login = requests.post(settings.CONTROL_ID_URL_LOGIN, data=login_data)

    if login.ok:
        session_id = login.json().get('session')
    else:
        raise ValueError(f'Login attempt error: {login.json()}')

    open = requests.post(
        f'{settings.CONTROL_ID_URL_DOOR}{session_id}',
        json=open_door_data)

    if open.ok:
        print(f'\n{settings.CONTROL_ID_URL_DOOR}{session_id}\n')
    else:
        raise ValueError(f'Login attempt error: {open.json(), open.url}')
