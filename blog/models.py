from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    user_ip=models.CharField(max_length=50)
    post_text = models.TextField(max_length=500)
    created_on=models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return str(self.user_ip)
    class Meta:
        verbose_name_plural = "posts"