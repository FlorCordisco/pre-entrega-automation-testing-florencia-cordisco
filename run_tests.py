import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_navegacion.py",
    "tests/test_carrito.py"
]

# Argumentod para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)