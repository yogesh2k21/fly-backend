from django.urls import path

from .views import TeachersView

urlpatterns = [
  path('assignments/', TeachersView.as_view(), name='teachers-assignments')
]
