from django.contrib.contenttypes.admin import GenericTabularInline

from file.models import Image, Document


class ImageInlineAdmin(GenericTabularInline):
    model = Image
    fields = ("file",)
    extra = 0


class DocumentInlineAdmin(GenericTabularInline):
    model = Document
    fields = ("docs",)
    extra = 0
