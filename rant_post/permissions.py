from rest_framework import permissions


class RantPostUpdateDeletePermissions(permissions.BasePermission):
    """ Object-level permission to allow user to only update their own posts """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author
