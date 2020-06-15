from django.db import models
class Entry(models.Model):

    title=models.CharField(max_length=255)
    link=models.CharField(max_length=255)
    class Meta:
      verbose_name_plural = "entries"
    def __str__(self):
        return self.link
