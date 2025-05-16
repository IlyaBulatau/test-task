from django.apps.config import AppConfig


class TaskAppConfig(AppConfig):
    name = "tasks"

    def ready(self) -> None:
        from drf_spectacular.extensions import OpenApiAuthenticationExtension

        from tasks.server_auth import ServerAuthentication

        class ServerAuthenticationExtension(OpenApiAuthenticationExtension):
            target_class = ServerAuthentication
            name = "Bearer"

            def get_security_definition(self, auto_schema):
                return {
                    "type": "apiKey",
                    "in": "header",
                    "name": "Authentication",
                }
