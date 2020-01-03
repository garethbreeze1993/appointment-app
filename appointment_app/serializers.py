from rest_framework import serializers
from appointment_app.models import Times, User, Appointment

class TimesSerializer(serailizers.ModelSerializer):
    class Meta:
        model = times
        fields = ('id', 'time_start', 'time_end', 'date_start')
        
        
class AppointmentSerializer(serailizers.ModelSerializer):
    times = TimesSerializer(many=False, read_only=False)
    client = serializers.ReadOnlyField(source='client.username')
    class Meta:
        model = Appointment
        fields = ('id', 'times', 'filled', 'client')
