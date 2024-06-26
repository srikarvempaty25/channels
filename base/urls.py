from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name = "register"),
    path('login/', views.loginUser, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),
    path('profile/<str:pk>', views.userProfile, name = "user-profile"),
    path('edit-user/', views.editUser, name = "edit-user"),
    path('delete-message/<str:pk>', views.deleteMessage, name = "delete-message"),
    path('', views.home, name = "home"),
    path('room/<str:pk>/', views.room, name = "room"),
    path('create-room/', views.createRoom, name = "create-room"),
    path('edit-room/<str:pk>/', views.editRoom, name = "edit-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name = "delete-room"),
]