from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    """
    Custom permission to only allow authors of a post to update it.
    """

    def has_object_permission(self, request, obj):
        # Check if the user is the author of the post
        return obj.author == request.user