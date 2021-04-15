from django.contrib import admin
from django.urls import path,include
from signup import views
from rest_framework_simplejwt.views import TokenobtainPairView,TokenrefreshView

urlpatterns = [
    path('',views.index,name='index'),
    path('FP',views.FP,name='FP'),
    path('SetP',views.SetP,name='SetP'),
    path('api/token/',TokenObtainPairView.as_view())
    path('api/token/refresh/',TokenRefreshView.as_view())
]
