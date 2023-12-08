from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Sum, Count

from .serializers import AddAvionSerializer
from ..models import ModelAvion, Societe

class AddAvion(APIView):
    def post(self, request):
        serializer = AddAvionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'data added succefully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'went problem with data', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class GetAvion(APIView):
    def get(self, requesr):
        avion = ModelAvion.objects.all()
        serializer = AddAvionSerializer(avion, many=True)
        return Response({'data': 'success get', 'data': serializer.data})

class dashboardView(APIView):
    def get(self, request):
        nbrAvionAir = ModelAvion.objects.filter(typeAir='airplane').count()

        nbrAvionMil = ModelAvion.objects.filter(typeAir='Melitairie').count()

        co2air = ModelAvion.objects.filter(typeAir='airplane').aggregate(total_co2=Sum('capacityOfFuel')*2.3)
        noxair = ModelAvion.objects.filter(typeAir='airplane').aggregate(total_nox=Sum('capacityOfFuel')*0.02)
        soxair = ModelAvion.objects.filter(typeAir='airplane').aggregate(total_sox=Sum('capacityOfFuel')*0.001)

        co2mil = ModelAvion.objects.filter(typeAir='melitairie').aggregate(total_co2=Sum('capacityOfFuel') * 2.3)
        noxmil = ModelAvion.objects.filter(typeAir='melitairie').aggregate(total_nox=Sum('capacityOfFuel') * 0.02)
        soxmil = ModelAvion.objects.filter(typeAir='melitairie').aggregate(total_sox=Sum('capacityOfFuel') * 0.001)

        # noiseAir = ModelAvion.objects.filter(typeAir=)

        data = {
            'numberAir': nbrAvionAir,
            'numberMil': nbrAvionMil,
            'CO2Air': co2air,
            'NOXAir': noxair,
            'SOXAir': soxair,

            'CO2Mil': co2mil,
            'NOXMil': noxmil,
            'SOXMil': soxmil,


        }

        return Response({'message': 'dashboard', 'data': data}, status=status.HTTP_200_OK)
