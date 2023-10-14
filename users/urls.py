from django.urls import path

from users import views

app_name = "user"

urlpatterns = [
    path("", views.UserList.as_view(), name="list"),
    path("<int:pk>/", views.UserDetail.as_view(), name="detail"),
]
