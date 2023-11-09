from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        app_label = 'blog1' 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        app_label = 'blog1'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField(Post)

    class Meta:
        app_label = 'blog1'
