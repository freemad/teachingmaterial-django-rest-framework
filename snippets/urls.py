from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = "snippet"

urlpatterns = [
    path("", views.SnippetList.as_view(), name="list"),
    path('<int:pk>/', views.SnippetDetail.as_view(), name="detail"),
    path('<int:pk>/highlight/', views.SnippetHighlight.as_view(), name="highlight"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
