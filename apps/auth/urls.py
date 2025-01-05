from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh') # Називаємо шлях назваАпки_дія
]
