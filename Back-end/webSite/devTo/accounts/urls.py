from django.urls import path
from .views import SignUpView, logoutUser

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', logoutUser, name="logout"),

]
