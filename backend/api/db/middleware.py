from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.conf import settings


class TokenManagementMiddleware(MiddlewareMixin):
    def process_request(self, request):
        jwt = request.session.get("jwt")
        if jwt and self.jwt_expired(jwt):
            response = self.refresh_jwt(jwt)
            if response.get("error"):
                return JsonResponse(
                    {"error": "Authentication failure, please log in again"}, status=401
                )
            request.session["jwt"] = response[
                "access_token"
            ]  # Update the session with the new JWT

    def jwt_expired(self, jwt):
        # Here you should implement the logic to determine if the JWT is expired
        # This can be done by decoding the JWT and checking the exp claim
        import jwt as jwt_lib

        try:
            jwt_decoded = jwt_lib.decode(
                jwt, settings.SUPABASE_SECRET, algorithms=["HS256"]
            )
            return jwt_decoded["exp"] < time.time()
        except jwt_lib.ExpiredSignatureError:
            return True
        except Exception as e:
            return True  # Safest to assume it needs refreshing if there's an error

    def refresh_jwt(self, jwt):
        # Use the Supabase client to refresh the token
        # Assuming `supabase` is globally available as `settings.SUPABASE_CLIENT`
        return settings.SUPABASE_CLIENT.auth.refresh_session(jwt)
