from django.urls import path
from predictor import views


urlpatterns = [
    path('', views.predict_diabetes, name='predict_diabetes')
]