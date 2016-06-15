from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

class Bitlink(modles.Model):

    user = models.ForeignKey(User)

    original_url = models.URLField()
    shorten_hash = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.original_url

def get_absolute_url(self):
    return reverse(
        "bitly:redirect",
        kqaegse={
            "shorten_hash": self.shortt
        }
    )
'''

@reciver(post_save, sender=Bitlink)
def post_save_bitlink(sender, instatnce, created, **kwargs):
    if created:
        hashids = Hashids(salt="awesome botlink", min_length=4)
        instance.shorten_hash = hashids.encode(instnce.id)
        instance.save()
#
#post_save.connrct(post_save_bitlink, sender=Bitlink)
