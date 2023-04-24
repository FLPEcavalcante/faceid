from rest_framework import response, status, views
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from django.http import Http404

from facial.models import DataRequest

from . import serializers, controlid


class OpenDoorView(views.APIView):
    """Method Class for open door action.

    Args:
        request (dict): Uses a data response list.

    Returns:
        queryset (JSON): return list of data FindFace.
    """

    def post(self, request):
        """Post data and open door.

        Args:
            request: request.

        Returns:
            response.Response: rest_framework Response.
        """

        try:
            controlid.ControlID.opendoor()
        except Exception as exc:
            return response.Response(
                {"error": exc}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = serializers.DataRequestSerializer(
            data=request.data, many=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def delete_all(self):
        """Delete all objects from the DataRequest model."""
        DataRequest.objects.all().delete()

    def delete(self, request):
        """Delete all objects from the DataRequest model."""
        self.delete_all()
        return response.Response(
            {"message": "All objects have been deleted."}, status=status.HTTP_204_NO_CONTENT
        )
    
# class ModelDelete(DestroyAPIView):
#     """
#     View for deleting objects of the DataRequest model.
#     """
    
#     queryset = DataRequest.objects.all()
#     serializer_class = serializers.DataRequestSerializer

#     def delete(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             self.perform_destroy(instance)
#         except Http404:
#             pass
#         return Response(status=status.HTTP_204_NO_CONTENT)
