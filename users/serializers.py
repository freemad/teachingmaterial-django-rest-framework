from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):

    snippets = serializers.HyperlinkedRelatedField(many=True, view_name="snippet:detail", read_only=True)

    class Meta:
        model = User
        fields = ("url", "id", "username", "snippets",)
        extra_kwargs = {"url": {"view_name": "snippet:detail"}}  # noqa essential for using beside app_name in urls (https://devlog.jwgo.kr/2019/11/08/how-to-set-default-url-field-when-using-appname-in-drf/)
