from django.urls import path

from .views import GetAvion, AddAvion, dashboardView

urlpatterns = [
    path('addAvion/', AddAvion.as_view(), name='add_avion'),
    path('getAvion/', GetAvion.as_view(), name='get_avion'),
    path('dashboard/', dashboardView.as_view(), name='dashboard')

    # path('login/', UserLoginView.as_view(), name='user_login'),
    # path('registerAdmin/', AdminRegisterView.as_view(), name='user_register'),
    # path('registerUser/', UserRegisterView.as_view(), name='user_register'),
    # path('user/<int:pk>/', GetSpecificUserView.as_view(), name='get_specific_user'),
    # path('changePassword/<int:pk>/', UserChangePasswordView.as_view(), name='change_password'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('resetPassword/<str:pk>/', UserResetPasswordView.as_view(), name='reset_password'),
    # path('sendOtp/', SendOtpView.as_view(), name='send_otp_via_email'),
    # path('verifyOtp/', VerifyOtpView.as_view(), name='verify_otp'),
    # path('modifyUser/<int:pk>/', ModifyUserProfileView.as_view(), name='modify_user_profile'),

]
