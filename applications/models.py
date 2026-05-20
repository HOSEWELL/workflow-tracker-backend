import uuid
from django.db import models
from .enums import APPLICATION_TYPES, STATUSES

class Application(models.Model):
    tracking_number = models.CharField(max_length=100, unique=True)
    applicant_name = models.CharField(max_length=255)
    applicant_email = models.EmailField()
    company_name = models.CharField(max_length=255)

    application_type = models.CharField(
        max_length=100,
        choices=APPLICATION_TYPES
    )

    description = models.TextField()

    status = models.CharField(
        max_length=50,
        choices=STATUSES,
        default="Draft"
    )

    reviewer_comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    submitted_at = models.DateTimeField(null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)