from django.contrib import admin

from .models import Feedback
from feedback.models import *
# Register your models here.
admin.site.register(Feedback)