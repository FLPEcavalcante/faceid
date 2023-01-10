import datetime

from django.contrib.auth.models import User
from model_mommy.recipe import Recipe

from facial import models, views


class DataRequestRecipes:
    """_summary_
    """

    def __init__(self):

        self.user = Recipe(
            User,
            is_staff=True,
            email='hexgis@gmail.com',
            password='top_secret',
        )

        self.data_request = Recipe(
            models.DataRequest,
            id='4491681447131583578',
            thumbnail='https://findface.hex.hex360/uploads/2023/01/09/face_event/132851_face_thumbnail_6pJcD1.jpg',
            fullframe='https://findface.hex.hex360/uploads/2023/01/09/face_event/132851_face_full_frame_lvLyQm.jpg',
            matched=True,
            created_date=datetime.datetime.now(),
            facial_creation_date=datetime.datetime.now(),
        )
