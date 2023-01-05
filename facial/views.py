from django.http import JsonResponse
from rest_framework import response, status, views
from django.conf import settings

from facial.control_id.views import authenticate

from facial.serializers import DataRequestSerializer


class OpenDoor(views.APIView):

    """Method Class for open door action.

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
