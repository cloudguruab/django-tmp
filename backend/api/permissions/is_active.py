from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated


class IsActive(IsAuthenticated):
    """
    Allows access only to authenticated & active users.
    """

    message = _(
        "You do not have permission to perform this action because your account "
        "is disabled."
    )

    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.is_active)
