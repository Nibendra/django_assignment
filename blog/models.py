from django.db import models


class Post(models.Model):
    post_name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    post_image = models.ImageField(upload_to='blog/images')
    post_body = models.TextField(max_length=1000)

    def __str__(self):
        return self.post_name
