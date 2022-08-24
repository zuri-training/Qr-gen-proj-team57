from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from . import views
import logging
from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed





@receiver(user_logged_in)
def log_user_logged_in(sender, request, user, **kwargs):
    # print('user {} logged in through page {}'.format(username, request.META.get('HTTP_REFERER')))
    print('user logged in')
    # logger.info("{} logged in with {}".format(user.email, request))

@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    # print('user {} failed to log in through page {}'.format(username, request.META.get('HTTP_REFERER')))
    print('user failed to log in')
user_login_failed.connect(log_user_login_failed)

@receiver(user_logged_out)
def log_user_logged_out(sender, request, user, **kwargs):
    # print('user {} logged out through page {}'.format(username, request.META.get('HTTP_REFERER')))
    print('user logged out')

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
