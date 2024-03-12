from django.urls import path
from .views import *

urlpatterns = [
    path('bolimlar/', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarViews.as_view(), name='mahsulotlar'),

    path('mahsulotlar/<int:pk>/tahrirlash/', MahsulotEditView.as_view()),
    path('mijozlar/<int:pk>/tahrirlash/', MijozEditView.as_view()),

    path('mijozlar/', MijozView.as_view(), name='mijozlar'),
    path('statistika/', StaticView.as_view(), name='statistika'),

    path('mahsulotlar/<int:pk>/delete/', MahsulotDeleteView.as_view()),
    path('mijoz/<int:pk>/delete/', MijozDeleteView.as_view()),

]
