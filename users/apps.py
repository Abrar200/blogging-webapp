from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(signals):
    	import users.signals