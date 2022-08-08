from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path("djangox/", HomePageView.as_view(), name="home"),
    path("djangox/about/", AboutPageView.as_view(), name="about"),
]
