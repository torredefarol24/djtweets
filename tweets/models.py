from django.db import models
import random 
from django.conf import settings

User = settings.AUTH_USER_MODEL

# class TweetLike

class Tweet(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE) # many users can have many tweets
      content = models.TextField(blank=True, null=True)
      image = models.FileField(upload_to="images/", blank=True, null=True)
      likes = models.ManyToManyField(User, related_name='tweet_user', blank=True)
      
      class Meta:
            ordering = ["-id"]


      def serialize(self):
            return {
                  "id" : self.id,
                  "content" : self.content,
                  "likes" : random.randint(0,544)
            }

      def __str__(self):
            return self.content