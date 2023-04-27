from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'candidate', views.CandidateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vote/', views.VoteView.as_view()),
    path('voters/', views.VotersView.as_view()),
    path('report/', views.reportView.as_view())
]
