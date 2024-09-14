from django.db import models


ACTION_TYPE_CHOICES = [
    ("CREATED", "CREATED"),
    ("UPDATED", "UPDATED"),
    ("DELETED", "DELETED"),
]

class BaseModel(models.Model):
    action_type = models.CharField(max_length=16, blank=True, choices=ACTION_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=36, blank=True, null=True)
    updated_by = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        abstract = True