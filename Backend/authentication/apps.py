from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

<<<<<<< HEAD
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
=======
    def ready(self):
        import authentication.signals
>>>>>>> 6016203fe5a9fce2e2b7045f849a5cca1226fccf
