from django.db.models.signals import post_save
from django.dispatch import receiver

from hashids import Hashids

from bitly.models.bitlink import Bitlink


@receiver(post_save, sender=Bitlink)
def post_save_bitlink(sender, instance, created, **kwargs):
    # bitlink instance.id => Hashids =>shorten_hash
    if created:
        # bitlink.id => bitlink.shorten_hash 생성( hash_id )
        hashids = Hashids(salt="awesome bitlenk", min_length=4)
        instance.shorten_hash = hashids.encode(instance.id)
        instance.save()
