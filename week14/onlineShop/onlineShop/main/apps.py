from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'onlineShop.main'

    def ready(self):
        import onlineShop.main.signals
