from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    default_app_config = 'home.apps.HomeConfig'
    name = 'home'

    def ready(self):
        import home.translation
