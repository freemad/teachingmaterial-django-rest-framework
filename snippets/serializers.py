from rest_framework import serializers

from snippets.models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name="snippet:highlight", format="html")

    class Meta:
        model = Snippet
        fields = ("url", "id", "owner", "highlight",
                  "title", "code", "linenos", "language", "style",)
        extra_kwargs = {"url": {"view_name": "snippet:highlight"}}  # noqa essential for using beside app_name in urls (https://devlog.jwgo.kr/2019/11/08/how-to-set-default-url-field-when-using-appname-in-drf/)
