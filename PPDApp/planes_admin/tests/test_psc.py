import pytest
from planes_admin.models import Plan
from django.db import IntegrityError

@pytest.mark.django_db
def test_plan_creacion_exitosa():
    plan = Plan.objects.create(nombre="Plan Agua", anio=2025, resolucion="123")
    assert plan.nombre == "Plan Agua"

@pytest.mark.django_db
def test_plan_requiere_anio():
    with pytest.raises(IntegrityError):
        Plan.objects.create(nombre="Sin Año")
