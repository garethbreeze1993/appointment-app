'''
from appointment_app.models import Times, Appointment
from appointment_app.serializers import AppointmentSerializer,TimesSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    

    def perform_create(self, app_info):
        app_info.save(client = self.request.user)
'''
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from appointment_app.models import Times, Appointment
from appointment_app.serializers import AppointmentSerializer,TimesSerializer

@api_view(['GET', 'POST'])
def appointment_list(request, format=None):
    """
    List all code appointments, or create a new snippet.
    """
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client_id = request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def appointment_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code appointment.
    """
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save(client_id=request.user.id)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        appointment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    




'''
example post request json object to send
 {
        "times": {
            "time_start": "15:00:00",
            "date_start": "2020-01-03"
        },
        "filled": false
    }
'''
