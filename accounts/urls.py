from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupAPIView

urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
