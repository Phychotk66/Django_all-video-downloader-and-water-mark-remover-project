from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    watermark_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
