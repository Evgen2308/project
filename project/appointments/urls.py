from django.urls import path
from .views import AppointmentView


urlpatterns = [
   path('', AppointmentView.as_view(), name='appointments'),
   path('make_appointment', AppointmentView.as_view(), name='make_appointment'),
   path('<int:pk>', AppointmentView.as_view(), name='appointment_create'),
]