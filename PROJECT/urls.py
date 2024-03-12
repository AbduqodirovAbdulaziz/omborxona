from django.contrib import admin
from django.urls import path, include

from userAPP.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('mainAPP.url')),
    path('user/', include('userAPP.url')),
    path('statistika/', include('statsAPP.url')),

    path('',LoginView.as_view(),name='login')
]
