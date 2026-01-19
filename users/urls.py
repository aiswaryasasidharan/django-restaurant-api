from django.urls import path
from .views import ( 
    MenuListCreate, MenuDetail, OrderListCreateAPIView,
    OrderDetailAPIView,TableBookingListCreateAPIView,TableBookingDetailAPIView)

urlpatterns = [
    path('menu/', MenuListCreate.as_view()),
    path('menu/<int:pk>/', MenuDetail.as_view()),
    path('orders/', OrderListCreateAPIView.as_view()),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view()),
    path('book/', TableBookingListCreateAPIView.as_view()),
    path('book/<int:pk>/', TableBookingDetailAPIView.as_view()),
]
