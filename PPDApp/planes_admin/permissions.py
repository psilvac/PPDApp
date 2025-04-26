from rest_framework.permissions import BasePermission, DjangoModelPermissions

class DjangoModelPermissionsWithRead(DjangoModelPermissions):
    perms_map = {
        # sobreescribe el perms_map de DjangoModelPermissions
        # agrega el permiso 'view_%(model_name)s' a los permisos de 'GET'
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

class EsMismoOrganismo(BasePermission):
    """
    Permite la acción solo si el usuario pertenece al mismo organismo que el objeto.
    """

    def has_permission(self, request, view):
        # Permitir solo a usuarios autenticados
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Controlar acceso en lectura y escritura en función del organismo
        return request.user.organismo == obj.organismo