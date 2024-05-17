from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RefreshTokenSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            result = supabase.auth.sign_in_with_password(email=email, password=password)
            if "user" in result:
                request.session["jwt"] = result[
                    "access_token"
                ]  # Storing JWT in session
                return Response(
                    {"message": "Logged in successfully"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshTokenView(APIView):
    def post(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        if serializer.is_valid():
            refresh_token = serializer.validated_data["refresh_token"]
            result = supabase.auth.refresh_session(refresh_token=refresh_token)
            request.session["jwt"] = result["access_token"]  # Update the JWT in session
            return Response(
                {"message": "Token refreshed successfully"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        jwt = request.session.pop("jwt", None)
        if jwt:
            supabase.auth.sign_out(jwt=jwt)  # Server-side JWT management if necessary
            return Response(
                {"message": "Logged out successfully"}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "User not logged in"}, status=status.HTTP_401_UNAUTHORIZED
        )
