from django.urls import path, include

urlpatterns = [
    path("v1/", include("core.api.v1.routers.lunch_credits_router")),
]
