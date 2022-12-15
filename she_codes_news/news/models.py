from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        USER, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")

    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(max_length=200, default="https://picsum.photos/600")
