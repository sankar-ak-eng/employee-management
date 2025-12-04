from rest_framework import serializers
from core.models import Employee, MonthlyBalance, LunchOrder
from core.utils.lunch_credits_utils import get_current_balance


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "monthly_allowance", "created_at", "updated_at"]


class BalanceSerializer(serializers.ModelSerializer):
    available_credits = serializers.IntegerField(read_only=True)

    class Meta:
        model = MonthlyBalance
        fields = [
            "year",
            "month",
            "starting_credits",
            "extra_credits",
            "used_credits",
            "available_credits",
        ]


class TopUpSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=0)

    def save(self, employee):
        balance = get_current_balance(employee)
        balance.extra_credits += self.validated_data["amount"]
        balance.save()
        return balance


class LunchOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = LunchOrder
        fields = [
            "id",
            "employee",
            "year",
            "month",
            "cost_credits",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        employee = attrs["employee"]
        cost = attrs["cost_credits"]
        balance = get_current_balance(employee)
        if balance.available_credits < cost:
            raise serializers.ValidationError("Not enough credits for this order.")
        return attrs

    def create(self, validated_data):
        employee = validated_data["employee"]
        cost = validated_data["cost_credits"]
        balance = get_current_balance(employee)
        # Deduct used credits
        balance.used_credits += cost
        balance.save()
        return super().create(validated_data)
