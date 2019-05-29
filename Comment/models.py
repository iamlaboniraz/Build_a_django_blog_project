from __future__ import unicode_literals

from django.conf import settings
from django.db import models


# Create your models here.
from posts.models import Posts

class Comment(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.PROTECT)
    post        = models.ForeignKey(Posts,on_delete=models.PROTECT)
    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.user.username)

    def __str__(self):
        return str(self.user.username)