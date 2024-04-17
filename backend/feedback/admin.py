from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "company_name", "is_solved"]
    list_filter = []
    ordering = ["id"]
    fieldsets = [
        (
            "FEEDBACK INFORMATION",
            {
                "fields": (
                    "title",
                    "description",
                    "company_name",
                    "is_solved",
                    "created_at",
                    "modified_at",
                )
            },
        ),
        (
            "CUSTOMER INFORMATION",
            {
                "fields": (
                    "customer_name",
                    "customer_email",
                    "customer_phone",
                )
            },
        ),
    ]

    def company_name(self, obj):
        return obj.organization.company_name
