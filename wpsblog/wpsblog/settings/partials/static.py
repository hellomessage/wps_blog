import os

from .base import PROJECT_ROOT_DIR
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(
    PROJECT_ROOT_DIR,
    "dist",
    "madia",
)
MEDIA_URL = '/media/'
