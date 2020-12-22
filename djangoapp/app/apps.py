from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'

    # To initiate signals
    def ready(self):
        import app.signals
