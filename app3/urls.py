from . import views
from django.urls import path
app_name="app3"

urlpatterns = [

    path('form', views.form, name='form'),

]