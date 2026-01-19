from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import MenuItem, Order, TableBooking
from .serializers import MenuItemSerializer, OrderSerializer, TableBookingSerializer


# MENU CRUD
class MenuListCreate(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


# ORDER CREATE
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        items = serializer.validated_data['items']
        total = sum(i.price for i in items)

        serializer.save(
            user=self.request.user,
            total_amount=total
        )


# RETRIEVE + UPDATE + DELETE
class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        items = serializer.validated_data.get('items')
        if items:
            total = sum(i.price for i in items)
            serializer.save(total_amount=total)
        else:
            serializer.save()


# TABLE BOOKING
class TableBookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# RETRIEVE + UPDATE + DELETE
class TableBookingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


