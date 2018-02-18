from django.conf import settings
from django.conf.urls import url

from .views import CalculationView

app_name = 'calculator'
urlpatterns = [
    url('calculate/', CalculationView.as_view(), name='calculation'),
]
