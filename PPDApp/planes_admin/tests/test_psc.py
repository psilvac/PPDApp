import pytest
from rest_framework.test import APIClient
from user.models import Usuario
from django.contrib.auth.models import Permission  # Agregado

@pytest.mark.django_db
def test_endpoint_con_autenticacion():
    client = APIClient()

    # 📌 Verificar que los permisos necesarios existen
    required_permissions = [
        'add_comuna',
        'change_comuna',
        'delete_comuna',
        'view_comuna'
    ]

    for codename in required_permissions:
        assert Permission.objects.filter(codename=codename).exists(), f"Permiso {codename} no existe."

    # Crear el usuario
    user = Usuario.objects.create_user(
        email="test@example.com",
        nombre="Test",
        apellido="User",
        password="password123"
    )

    # Login para obtener el token
    response = client.post('/api/token/', {
        'email': 'test@example.com',
        'password': 'password123'
    })

    assert response.status_code == 200, response.data

    token = response.data['access']  # Para JWT estándar

    # Agregar token en los headers
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    # Probar un endpoint protegido
    protected_response = client.get('/api/comunas/')

    assert protected_response.status_code == 200
