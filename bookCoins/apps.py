from django.apps import AppConfig


class BookcoinsConfig(AppConfig):
    name = 'bookCoins'

    def ready(self):
        import bookCoins.signals

