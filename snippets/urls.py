from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = "snippet"

snippet_list = views.SnippetViewSet.as_view({
    "get": "list",
    "post": "create",
})
snippet_detail = views.SnippetViewSet.as_view({
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
})
snippet_highlight = views.SnippetViewSet.as_view({
    "get": "highlight",
}, renderer_classes=[renderers.StaticHTMLRenderer, ])


urlpatterns = format_suffix_patterns([
    path("", snippet_list, name="list"),
    path("<int:pk>/", snippet_detail, name="detail"),
    path("<int:pk>/highlight/", snippet_highlight, name="highlight"),
])
