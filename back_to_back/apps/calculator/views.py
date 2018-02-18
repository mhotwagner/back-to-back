from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Calculation
from .serializers import CalculationSerializer


class CalculationView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        number = request.GET.get('number', None)

        if number is None:
            return Response('<number> parameter is missing', status=400)

        try:
            number = int(number)
        except (TypeError, ValueError):
            return Response('<number> must be an integer', status=400)

        if number < 1 or number > 100:
            return Response('<number> must be integer between 1 and 100', status=400)

        calculation, _ = Calculation.objects.get_or_create(id=number)

        serializer = CalculationSerializer(calculation)

        # serializer.data is evaluated lazily
        # so we store it ahead of the save
        # in order to get the right occurrences and last_occurrence
        data = serializer.data

        calculation.increment_occurrences()
        calculation.save()

        return Response(data, status=200)


