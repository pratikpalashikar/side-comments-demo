from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

class Blog(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    body = models.TextField()
    comments = GenericRelation(Comment)

