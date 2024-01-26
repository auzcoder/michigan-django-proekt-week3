from hashlib import md5
from django import template

# https://brobin.me/blog/2016/07/super-simple-django-gravatar/

# A "gravatar" is a globally recognized avatar that is based on email address
# People must register their email address and then upload a gravatar
# If an email address has no gravatar, a generic image is put in its place

# To use the gravatar filter in a template include
# {% load app_tags %}

register = template.Library()


@register.filter(name='gravatar')
def gravatar(user, size=35):
    email = str(user.email.strip().lower()).encode('utf-8')
    email_hash = md5(email).hexdigest()
    url = "https://s.gravatar.com/avatar/87cdecb86c8acb493a908027d1beccff?s=80"
    return url.format(email_hash, size)
