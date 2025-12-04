from core.models import MonthlyBalance
from django.utils import timezone


def get_current_balance(employee):
    """
    Returns the MonthlyBalance instance for current month/year.
    Creates one if not exists with starting_credits = employee.monthly_allowance.
    """
    now = timezone.now()
    balance, created = MonthlyBalance.objects.get_or_create(
        employee=employee,
        year=now.year,
        month=now.month,
        defaults={"starting_credits": employee.monthly_allowance},
    )
    return balance
