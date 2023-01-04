from django.conf import settings
import requests
from facial import models, views


class RequestOpenDoor():

    # def __init__(self):

    #     # self.facial = xx
    #     # self.login_data = yy
    #     # self.open_door_data = ss
    #     print(self.login_data)

    # def xpto(self):
    #     print(self.authh)
    auth = models.Authentication.objects.filter(is_active=True).first()
    print("\n\n\n\n\---1--------------------->>>>>>>>>>>>>>>>>>>---------------")

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

    def authenticate(self):
        """Method for validated authencication of login the user.

        Args:
            login_data(JSON):

        Return:
            value (session): return a value for session validated.
        """
        print("\n\n\n\n\----2-------------------->>>>>>>>>>>>>>>>>>>---------------")

        login = requests.post(
            settings.CONTROL_ID_URL_LOGIN,
            RequestOpenDoor.login_data
        )
        print("\n\n\n\n\----3-------------------->>>>>>>>>>>>>>>>>>>---------------")
        print(login)

        if login.ok:
            import pdb
            pdb.set_trace()
            print("\n\n\n\n\---4--------------------->>>>>>>>>>>>>>>>>>>---------------")
            breakpoint()
            session_id = login.json().get('session')
        else:
            print("\n\n\n\n\----5-------------------->>>>>>>>>>>>>>>>>>>---------------")
            raise ValueError(f'Login attempt error: {login.json()}')

        open = requests.post(
            f'{settings.CONTROL_ID_URL_DOOR}{session_id}',
            json=RequestOpenDoor.open_door_data
        )

        if open.ok:
            print("\n\n\n\n\--6---------------------->>>>>>>>>>>>>>>>>>>---------------")
            print(f'\n{settings.CONTROL_ID_URL_DOOR}{session_id}\n')
        else:
            print("\n\n\n\n\---7--------------------->>>>>>>>>>>>>>>>>>>---------------")
            raise ValueError(f'Login attempt error: {open.json(), open.url}')
