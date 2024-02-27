# from django.contrib import admin

# from .models import Organization, OrganizationContact
# from file.admin import ImageInlineAdmin, DocumentInlineAdmin

# Register your models here.
# class ProfilePicInline(ImageInlineAdmin):
#     verbose_name = 'Profile Picture'
#     verbose_name_plural = 'Profile Picture'
#     max_num = 1

# @admin.register(Organization)
# class OrganizationAdmin(admin.ModelAdmin):
#     list_display = ['id', 'company_name', 'email']
#     list_filter = []
#     ordering = ['id']
#     inlines = [ProfilePicInline, OrganizationContact]
#     fieldsets = [
#         ('ORGANIZATION INFORMATION', {
#             'fields': ('company_name', 'email', 'address',)
#         }),
#         ('ORGANIZATION CONTACT', {
#             'fields': ('contact_name', 'phone', 'position',)
#         }),
#     ]
