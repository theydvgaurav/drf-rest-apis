from django.urls import path, include
from rest_framework import routers
from .views import UserSignUpView, LoginView
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('',UserSignUpView)

urlpatterns = [
   path('register/',include(router.urls)),
   path('login/', LoginView.as_view())
]