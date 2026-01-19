from django.db import models
from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"


class TableBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    status = models.CharField(max_length=20, default='Booked')

    def __str__(self):
        return f"{self.user.username} - {self.date}"

