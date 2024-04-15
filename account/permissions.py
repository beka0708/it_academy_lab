from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            if request.user == obj.user:
                return True
        except:
            if request.user == obj:
                return True





