from django.contrib.auth.models import AnonymousUser

from rest_framework import authentication, exceptions, request
from django.conf import settings


class ServerUser(AnonymousUser):
    @property
    def is_authenticated(self):
        return True


class ServerAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: request.Request):
        auth = str(request.META.get("HTTP_AUTHENTICATION", ""))

        user = ServerUser()

        if str(request.META.get("PATH_INFO")).startswith(
            ("/api/v1/docs/", "/api/v1/swagger/", "/static")
        ):
            return user, None

        if not auth or auth.lower() != settings.API_KEY:
            raise exceptions.AuthenticationFailed(
                "Invalid token header. No credentials provided."
            )

        return user, None
