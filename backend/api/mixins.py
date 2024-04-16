from .permissions import IsStaffEditor
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permissions_classes = [permissions.AllowAny , IsStaffEditor]