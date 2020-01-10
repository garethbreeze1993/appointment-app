import datetime
from rest_framework import serializers
from appointment_app.models import Times, Appointment

CHOICES_TIME_START = (
    (datetime.time(9), datetime.time(9)),
    (datetime.time(15), datetime.time(15)),
    (datetime.time(11), datetime.time(11)),
)

class TimesSerializer(serializers.ModelSerializer):
    time_start = serializers.ChoiceField(choices=CHOICES_TIME_START)
    class Meta:
        model = Times
        fields = ('id', 'time_start', 'time_end', 'date_start')
        
class UserSerializer(serializers.ModelSerializer):
    pass
        
        
class AppointmentSerializer(serializers.ModelSerializer):
    times = TimesSerializer()
    client = serializers.ReadOnlyField(source='client.username')
    class Meta:
        model = Appointment
        fields = ('id', 'times', 'filled', 'client')
        
    def create(self, validated_data):
        times_data = validated_data.pop('times')
        print('gbbggghg')
        print(times_data)
        time = TimesSerializer.create(TimesSerializer(), validated_data=times_data)
        appointment = Appointment.objects.create(times=time, **validated_data)
        return appointment
    
    def update(self, instance, validated_data):
        pass

# https://www.youtube.com/watch?v=EyMFf9O6E60

#{'times': OrderedDict([('get_time_start_display', '9AM'), ('date_start', datetime.date(2020, 1, 1))]), 'filled': False, 'client': <SimpleLazyObject: <User: aladdin>>}
#OrderedDict([('get_time_start_display', '9AM'), ('date_start', datetime.date(2020, 1, 5))])

# Try doing datetime.time object as parameter on models choices
