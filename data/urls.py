from django.urls import path
from . import views


urlpatterns = [
    path("data/", views.GetData.as_view()),
    path("", views.get_all)
]
