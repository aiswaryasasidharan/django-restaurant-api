from rest_framework import serializers
from .models import MenuItem, Order, TableBooking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TableBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableBooking
        fields = '__all__'
