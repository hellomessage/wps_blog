'''
#from django.db import models
#from django.core.urlresolvers import reverse
#
#
#class Post(models.Model):
#
#    objects = PostManager()
#
#    title = models.CharField(
#        max_length=120,
#    )
#
#    content = models.TextField()
#    shorten_hash = models.CharField(
#        max_length = 8,
#        blank=True,
#        null=True,
#    )
#
#    is_public = models.BooleanField(
#        default=True,
#    )
#
#    def __str__(self):
#        return self.title
#
#    def get_original_url(self):
#        return reverse(
#            "posts:detail",
#            kwargs={
#                "post_id": self.id,
#            }
#        )
#
#    def get_shorten_url(self):
#        return reverse(
#            "posts:update",
#            kwargs={
#                "post_id": self.id,
#            }
#    
#    def get_image_url(self):
#        if self.image:
#            return self.image.url
#        return "http://placehold.it/300x200"
#
'''
