from django.contrib.auth.models import User
from rest_framework import viewsets

from users.serializers import UserSerializer


# Create your views here.

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This ViewSet automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
