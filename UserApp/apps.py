from django.apps import AppConfig


class UserappConfig(AppConfig):
    name = 'UserApp'

    def ready(self):
        import UserApp.signals
