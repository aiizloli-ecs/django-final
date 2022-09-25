from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    short_description = models.TextField()
    image = models.ImageField(upload_to="cover/",
                              null=True,
                              blank=True)
    content = models.TextField(null=True, 
                               blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}: {self.title}"