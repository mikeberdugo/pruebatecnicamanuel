from django.urls import path

from . import views

urlpatterns = [
    path('',views.Fibonacci.as_view(),name='serie'),
]


