from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, RegisterView, ProtectedView
#from .views import register, profile


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='ryzhiki_1/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'), # И здесь
    path('protected/', ProtectedView.as_view(), name='protected'),
]