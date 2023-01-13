from django.urls import path
from .views import *

urlpatterns = [
    path("create-requesters-request", CreateRequestersRequestView.as_view()),
    path("create-rider-request", CreateRiderRequestView.as_view()),
    path("get-requesters-request", GetRequestersRequestView.as_view()),
    path("get-rider-request", GetRiderRequestView.as_view()),
    path("update-rider-request", UpdateRiderRequestView.as_view()),
]
