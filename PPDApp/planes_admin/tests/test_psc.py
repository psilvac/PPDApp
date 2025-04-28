import pytest
from rest_framework.test import APIClient
from user.models import Usuario  # O como se llame tu modelo de usuario


@pytest.mark.django_db
def test_endpoint_con_autenticacion():
    client = APIClient()

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