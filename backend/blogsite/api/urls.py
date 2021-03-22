from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.ApiPostDV.as_view(), name='post_detail'),
    path('tag/cloud/', views.ApiTagCloudLV.as_view(), name='tag_cloud'),

    path('login/', views.ApiLoginView.as_view(), name='login'),
    path('register/', views.ApiRegisterView.as_view(), name='register'),
]