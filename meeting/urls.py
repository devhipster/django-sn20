from django.urls import path
from . import views
urlpatterns = [ 
    path('meeting', views.testing),
    path('meet', views.index)
]