from django.contrib.auth.models import Group, Permission


def ensure_group(group_name: str, permissions: list[str]):
    """
    Ensures a group exists and has the supplied permissions.
    """

    group, _ = Group.objects.get_or_create(name=group_name)

    group.permissions.set(
        [Permission.objects.get(codename=perm) for perm in permissions]
    )
