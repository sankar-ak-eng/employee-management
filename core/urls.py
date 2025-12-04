from django.urls import path, include

urlpatterns = [
    path("api/", include("core.api.v1.routers")),
]
