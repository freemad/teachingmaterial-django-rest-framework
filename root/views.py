from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def root(request, format=None):
    return Response({
        "users": reverse("user:list", request=request, format=format),
        "snippets": reverse("snippet:list", request=request, format=format),
    })
