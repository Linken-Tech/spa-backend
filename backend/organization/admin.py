from django.contrib import admin

from .models import Organization, OrganizationContact
from file.admin import ImageInlineAdmin


class ProfilePicInline(ImageInlineAdmin):
    verbose_name = "Profile Picture"
    verbose_name_plural = "Profile Picture"
    max_num = 1


class ContactIncline(admin.TabularInline):
    model = OrganizationContact
    fields = (
        "contact_name",
        "phone",
        "position",
        "created_at",
        "modified_at",
    )
    extra = 0


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["id", "company_name", "email"]
    list_filter = []
    ordering = ["id"]
    inlines = [ProfilePicInline, ContactIncline]
    fieldsets = [
        (
            "ORGANIZATION INFORMATION",
            {
                "fields": (
                    "company_name",
                    "email",
                    "address",
                    "created_at",
                    "modified_at",
                )
            },
        )
    ]
