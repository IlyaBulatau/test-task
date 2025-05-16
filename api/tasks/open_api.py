from drf_spectacular.extensions import OpenApiAuthenticationExtension
from tasks.server_auth import ServerAuthentication


class SimpleJWTTokenUserScheme(OpenApiAuthenticationExtension):
    target_class = ServerAuthentication

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "in": "header",
            "name": "Authentication",
        }
