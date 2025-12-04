from django.db import models
from django.utils import timezone
from .base import BaseModel


class Employee(BaseModel):
    name = models.CharField(max_length=255)
    monthly_allowance = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class MonthlyBalance(BaseModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="balances"
    )
    year = models.IntegerField()
    month = models.IntegerField()
    starting_credits = models.PositiveIntegerField()
    extra_credits = models.PositiveIntegerField(default=0)
    used_credits = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("employee", "year", "month")

    @property
    def available_credits(self):
        return self.starting_credits + self.extra_credits - self.used_credits

    def __str__(self):
        return f"{self.employee.name} - {self.year}/{self.month}"


class LunchOrder(BaseModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="orders"
    )
    year = models.IntegerField()
    month = models.IntegerField()
    cost_credits = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        # Automatically set current month/year if not provided
        now = timezone.now()
        if not self.year:
            self.year = now.year
        if not self.month:
            self.month = now.month
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.name} - {self.cost_credits} credits ({self.month}/{self.year})"
