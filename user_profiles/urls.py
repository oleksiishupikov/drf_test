from django.urls import path

from .views import UserDetail, UserList, RegisterUser

app_name = 'user_profiles'

urlpatterns = [
    path('sign-in', RegisterUser.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]
