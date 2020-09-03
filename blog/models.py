from django.db import models

class blog_post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title