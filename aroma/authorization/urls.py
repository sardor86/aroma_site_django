from django.urls import path

from .views import login, registration

urlpatterns = [
    path('/login', login, name='home'),
    path('/registration', registration, name='home'),
]
