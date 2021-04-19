from django.urls import path
from . import views 
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('jordan/', views.JordanList.as_view(), name='jordan_list'),
    path('puma/', views.PumaList.as_view(), name='puma_list'),
    path('nike/', views.NikeList.as_view(), name='nike_list'),
    path('jordan/<int:pk>', views.JordanDetail.as_view(), name='jordan_detail'),
    path('puma/<int:pk>', views.PumaDetail.as_view(), name='puma_detail'),
    path('nike/<int:pk>', views.NikeDetail.as_view(), name='nike_detail'),
]
