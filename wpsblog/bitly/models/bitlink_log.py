from django.db import models


class BitlinkLog(models.Model):
    # 같은 어플리캐이션 안에 있으므로 스트링으로 받음 즉 "Bitlink"
    bitlink = models.ForeignKey("Bitlink")
    # HTTP_REFERRER
    # HTTP_USER_AGENT
    # REMOTE_ADDR
    # META ( dict => json )
    http_referer = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    http_user_agent = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    http_remote_address = models.CharField(
        max_length=31,
        blank=True,
        null=True,
    )

    http_meta_json = models.TextField(blank=True, null=True,)
    created_at = models.DateTimeField(auto_now_add=True)
