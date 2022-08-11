import logging
from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from . import views

logger = logging.getLogger(__name__)


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