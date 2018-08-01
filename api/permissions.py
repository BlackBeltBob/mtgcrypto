from rest_framework import permissions

class MTGCryptoAdminPermission(permissions.BasePermission):
    message = 'MTGCrypto admin credentials required for this action.'

    def has_permission(self, request, view):
        # We disallow certain api functions for anyone who isn't staff.
        return request.user.is_staff
