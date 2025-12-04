from rest_framework import routers
from core.api.v1.views.lunch_credits_views import EmployeeViewSet, LunchOrderViewSet

router = routers.DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employee")
router.register(r"lunch-orders", LunchOrderViewSet, basename="lunchorder")

urlpatterns = router.urls
