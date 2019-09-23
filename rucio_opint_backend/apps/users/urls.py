from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token

from .views import current_user, UserList


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]
