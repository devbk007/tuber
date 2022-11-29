from django.urls import path
from . import views

urlpatterns = [
    path('hiretuber', views.hiretuber, name='hiretuber'),
    path('updatestatus/<int:id>', views.updatestatus, name='updatestatus'),
]