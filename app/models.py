from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title}, {self.content}, {self.created_at}"