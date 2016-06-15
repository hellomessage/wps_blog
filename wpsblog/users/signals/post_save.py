from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatc import receiver

from users.models.user_profile import UserProfile


@receiver(post_save, sender=User)
def post_save_user(sender, instance, create, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(
            user=instance,
        )
