from rest_framework import serializers
from file.models import Image, Document


class ImageSerializer(serializers.ModelSerializer):
    file = serializers.CharField()

    class Meta:
        model = Image
        fields = ["id", "file", "name"]


class DocsSerializer(serializers.ModelSerializer):
    docs_file = serializers.CharField()

    class Meta:
        model = Document
        fields = ["id", "docs_file", "name"]
