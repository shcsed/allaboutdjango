from django.urls import include, path

from . import views

app_name = "core"
api_urlpatterns = [
    path("weather/", views.WeatherAPIView.as_view(), name="weather"),
    path("server-distro/", views.ServerDistroAPIView.as_view(), name="server-distro"),
    path("devlogs/", views.DevlogListAPIView.as_view(), name="devlogs"),
    path("visits/", views.VisitsAPIView.as_view(), name="visits"),
]

urlpatterns = [
    path("redir/<str:to_alias>/", views.simple_redirect, name="simple_redirect"),
    path("api/", include(api_urlpatterns)),
]
