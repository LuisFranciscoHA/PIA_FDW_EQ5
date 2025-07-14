import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PIA.settings")
django.setup()

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from paginaoracle1.models import tecnologia_apoyo

admin_username = "admin"
admin_email = "admin@correo.com"
admin_password = "123"

if not User.objects.filter(username=admin_username).exists():
    User.objects.create_superuser(admin_username, admin_email, admin_password)
    print("Superusuario creado.")
else:
    print("El superusuario ya existe.")

supervisor_username = "supervisor"
supervisor_email = "supervisor@correo.com"
supervisor_password = "123"

if not User.objects.filter(username=supervisor_username).exists():
    supervisor_user = User.objects.create_user(
        username=supervisor_username,
        email=supervisor_email,
        password=supervisor_password,
        is_staff=True
    )

    supervisor_group, _ = Group.objects.get_or_create(name="Supervisor")
    supervisor_group.permissions.clear()

    ct = ContentType.objects.get_for_model(tecnologia_apoyo)

    add_perm = Permission.objects.filter(content_type=ct, codename__startswith="add_")
    supervisor_group.permissions.add(*add_perm)

    supervisor_user.groups.add(supervisor_group)
    print("Usuario Supervisor creado con permisos limitados (solo agregar tecnología).")
else:
    print("El usuario Supervisor ya existe.")


empleado_username = "empleado"
empleado_email = "empleado@correo.com"
empleado_password = "123"

if not User.objects.filter(username=empleado_username).exists():
    empleado_user = User.objects.create_user(
        username=empleado_username,
        email=empleado_email,
        password=empleado_password,
        is_staff=True
    )

    empleado_group, _ = Group.objects.get_or_create(name="Empleado")
    empleado_group.permissions.clear()

    ct = ContentType.objects.get_for_model(tecnologia_apoyo)

    view_perm = Permission.objects.filter(content_type=ct, codename__startswith="view_")
    empleado_group.permissions.add(*view_perm)

    empleado_user.groups.add(empleado_group)
    print("Usuario Empleado creado (solo puede ver tecnologías).")
else:
    print("El usuario Empleado ya existe.")
