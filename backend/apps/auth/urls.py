from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from apps.auth.views import ActivateUserView, RecoverByEmailView, UserRecoveryView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='auth_login'),
    path('/refresh', TokenRefreshView.as_view(), name='auth_refresh'),
    path('/activate/<str:token>', ActivateUserView.as_view(), name='activate_user'),

    path('/recover/<str:email>', RecoverByEmailView.as_view(), name='recover_by_email'),
    path('/recovery/<str:password>/<str:token>', UserRecoveryView.as_view(), name='user_recovery')
]
