from django.contrib.auth.models import User
from django.db import models
# model이 create될 때
from django.db.models.signals import post_save
# from django.dispatch import receiver


class UserProfile(models.Model):

    user = models.OneToOneField(User)

    phonenumber = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )

    address = models.CharField(
        max_length=64,
        blank=True,
        null=True,
    )


def post_save_user(sender, instance, created, **kwargs):

    if created:
        user_profile = UserProfile.objects.create(
            user=instance,
        )

post_save.connect(post_save_user, sender=User)
