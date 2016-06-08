from django.db import models


class Comment(models.Model):

    post = models.ForeignKey("Post")

    contnet = models.TextField()

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse(
            "post-detail",
            kwargs={
                "post_id": self.id,
            }
        ) + "#comment-" + str(self.id)
