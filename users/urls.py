from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, VerificationView, expectation

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('<int:pk>/verification/<code>', VerificationView.as_view(), name='verification'),
    path('expectation', expectation, name='expectation'),
]
