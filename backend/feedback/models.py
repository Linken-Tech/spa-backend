from django.db import models

# Create your models here.

# create a feedback table
"""
refer other models.py
"""


class Feedback(models.Model):
    user_email = models.EmailField(null=False)
    feedback_title = models.CharField(max_length=50)
    feedback_detail = models.CharField(max_length=255)
    feedback_status = models.BooleanField(default="False")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feedback_title
