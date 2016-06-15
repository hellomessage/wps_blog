from django.contrib.auth.models import User
from django.db import models
from django.db.modles.signals import Post_save
from django.dispatch import receiver

Class UserProfile(models.Model):
        
        blank=True,
        null=True
    )


    @receiver(post_save, sender=User)
    def post_save_user(sender, instance, created, **kwargs):
        if created:
            user_profile = UserProfile.objects.create(
                user=instance,
            )

