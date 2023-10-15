from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer


# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    """
        This ViewSet automatically provides `list`, `create`, `retrieve`,
        `update` and `destroy` actions.

        Additionally also an extra `highlight` action is provided.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, methods=["GET", ], renderer_classes=[renderers.StaticHTMLRenderer, ])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
