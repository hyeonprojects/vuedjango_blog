from .base import *

# TODO 환경에 맞게 수정을 해야합니다.

SECRET_KEY = 'u9#8^-pezo%ly^+-!a_y@^+#!x-(duba-%b_xj95z5@^9y=c1#'

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}