from django.contrib.contenttypes import fields
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from file.utils import vehicle_image_upload_path, vehicle_document_upload_path


class BaseMedia(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)

    name = models.CharField(_("File Name"), max_length=255)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey("content_type", "object_id")
    company = models.ForeignKey("organization.Organization", on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.name)
        super().delete()

    @classmethod
    def create_file(cls, file, obj, filename=None):
        if not filename:
            filename = file.name
        cls.objects.create(file=file, name=filename, content_object=obj)


class Image(BaseMedia):
    file = models.ImageField(upload_to=vehicle_image_upload_path)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")


class Document(BaseMedia):
    docs_file = models.FileField(upload_to=vehicle_document_upload_path)

    class Meta:
        verbose_name = _("Document")
        verbose_name_plural = _("Document")
