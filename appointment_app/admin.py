from django.contrib import admin
from appointment_app.models import Appointment, Times, User

admin.site.register(Appointment)
admin.site.register(Times)
admin.site.register(User)

