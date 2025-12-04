from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from core.models import Employee, LunchOrder
from core.api.v1.serializers import (
    EmployeeSerializer,
    LunchOrderSerializer,
    BalanceSerializer,
    TopUpSerializer,
)
from core.utils.lunch_credits_utils import get_current_balance


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=True, methods=["get"])
    def balance(self, request, pk=None):
        """GET /api/v1/employees/<id>/balance/"""
        employee = self.get_object()
        balance = get_current_balance(employee)
        serializer = BalanceSerializer(balance)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def topup(self, request, pk=None):
        """POST /api/v1/employees/<id>/topup/"""
        employee = self.get_object()
        serializer = TopUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        balance = serializer.save(employee=employee)
        return Response(BalanceSerializer(balance).data, status=status.HTTP_200_OK)


class LunchOrderViewSet(viewsets.ModelViewSet):
    queryset = LunchOrder.objects.all()
    serializer_class = LunchOrderSerializer
    permission_classes = [IsAuthenticated]
