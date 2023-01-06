from django.conf import settings
import requests
from facial import models, views


class ControlID:

    @staticmethod
    def get_open_door_data(
        id: int = 65793,
        reason: int = 3,
        timeout: int = 5000
    ) -> dict:
        """Get open door data for requests.

        Args:
            id (int, optional): request identifier. Defaults to 65793.
            reason (int, optional): open door reason. Defaults to 3.
            timeout (int, optional): timeout. Defaults to 5000.

        Returns:
            dict: open door data.
        """

        return {
            'actions': [
                {
                    'action': 'sec_box',
                    'parameters': f'id={id},reason={reason},timeout={timeout}'
                }
            ]
        }

    @staticmethod
    def get_login_data(
        username: str = settings.CONTROL_ID_USERNAME,
        password: str = settings.CONTROL_ID_PASSWORD
    ) -> dict:
        """Get login data object to request.

        Args:
            username (str, optional): username.
                Defaults to settings.CONTROL_ID_USERNAME.
            password (str, optional): password.
                Defaults to settings.CONTROL_ID_PASSWORD.

        Returns:
            dict: login object data.
        """

        return {
            'login': username,
            'password': password
        }

    @staticmethod
    def get_session_id():
        """Method to validate authencication for user.

        Raises:
            ValueError: Login attempt error.

        Return:
            value (session): return a value for session validated.
        """

        response = requests.post(
            settings.CONTROL_ID_URL_LOGIN,
            data=ControlID.get_login_data()
        )

        if response.ok:
            return response.json().get('session')
        else:
            raise ValueError(f'Login attempt error: {response.json()}')

    @staticmethod
    def opendoor() -> dict:
        """Open model data request.

        Raises:
            ValueError: Login attempt error.
            ValueError: Error while trying to open door.

        Returns:
            dict: response json.
        """

        response = requests.post(
            f'{settings.CONTROL_ID_URL_DOOR}{ControlID.get_session_id()}',
            json=ControlID.get_open_door_data()
        )

        if response.ok:
            return response.json()
        else:
            raise ValueError(
                f'Error while trying to open door: {response.json}')
