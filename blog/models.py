from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.TextField(max_length=300)
    post_date = models.DateTimeField()
    post_text = models.CharField(max_length=300)
    post_image = models.ImageField(upload_to='event_images/')


    def get_someText(self):

        return self.post_text[:50]
