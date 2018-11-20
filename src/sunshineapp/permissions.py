from rest_framework.permissions import BasePermission

'''class IsOwnerOrReadOnly(BasePermission):
    message='you must be the owner of this object'
    def has_object_permission(self,request,view,obj):
        return obj.owner==request.user'''

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj == request.user
        else:
            return False