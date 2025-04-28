# user/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,User, Permission
from django.contrib.contenttypes.models import ContentType

from django.db import models
from planes_admin.models import Organismo

class UsuarioManager(BaseUserManager):
    """
    Representa al administrador de usuarios.

    Métodos:
    - create_user: Crea un usuario en la base de datos.
    - create_superuser: Crea un super usuario en la base de datos.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Crea usuario en la base de datos

        Atributos:
            - email (str): Correo electrónico del usuario.
            - password (str): Contraseña del usuario.
                - extra_fields: Campos con información extra del usuario.

        Retorno:
            usuario object.
        """
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)

        if password:  # <<< agregado: validamos si viene contraseña
            usuario.set_password(password)  # <<< se mantiene
        else:
            usuario.set_unusable_password()

        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea un superusuario con permisos de administrador.

        Atributos:
            - email (str): Correo electrónico del usuario.
            - password (str): Contraseña del usuario.
            - extra_fields: Campos con información extra del usuario.

        Retorno:
            Usuario object.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # <<< agregado: validar que los superusuarios tengan is_staff e is_superuser correctamente
        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    """
    Representa un usuario del sistema.

    Campos:
        - email (str): Correo electrónico del usuario.
        - nombre (str): Nombre del usuario.
        - apellido (str): Apellido del usuario.
        - is_active (bool): Estado de vigencia del usuario.
        - is_staff (bool): Estado de pertenencia al grupo administrador.
        - clave_unica (str): Clave única del usuario.
        - organismo (int): Identificador del organismo sectorial al que pertenece el
        usuario.
    """

    list_display = ('email', 'nombre', 'apellido')

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    clave_unica = models.CharField(max_length=100)
    organismo = models.ForeignKey('planes_admin.Organismo',on_delete=models.SET_NULL,
        null=True,                 # Permite valores nulos en la base de datos
        blank=True                 # Permite dejar este campo vacío en formularios
    )


    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    class Meta:
        permissions = [
            ('crear_plan', 'Puede crear planes'),
            ('aprobar_plan', 'Puede aprobar planes'),
            ('actualizar_medidas', 'Puede actualizar estados de medidas'),
            ('administrar', 'Puede administra sistema'),

        ]

    def save(self, *args, **kwargs):
        # <<< agregado: encripta la contraseña si no está encriptada
        if self.pk is None or not self.password.startswith('pbkdf2_sha256') and not self.is_superuser:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email + " - " + self.nombre + "  " + self.apellido