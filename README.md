# Entrega-automation-testing-florencia-cordisco
Repositorio creado para realizar una pre-entrega para el curso Automation Testing dictado por Agencia de Habilidades para el Futuro de Buenos Aires Aprende

El propósito del proyecto es dar a conocer lo aprendido,
donde se desarrollan test de el login, la navegación básica, test del carrito de compra, con datos desde csv y json 
Web: saucedemo.com
Datos: 
        usuario: "standard_user"
        contraseña: "secret_sauce"            

## Tecnologías Requeridas:

-Python como lenguaje principal

-Pytest para estructura de testing: instalar desde la terminal con el comando 
pip install pytest-html

-Selenium WebDriver para automatización: desde la terminal instalar 
pip install selenium
pip install webdriver-manager

- Biblioteca Requests para pruebas de API: desde la terminal con el comando
pip install requests

-Git y GitHub para control de versiones

-CSV / JSON

## Reporte en HTML
Instalar: pip install pytest-html
Ejecutar: pytest --html=report.html --self-contained-html

--html=report.html establece el nombre del archivo
--self-contained-html incrusta CSS y JS, de modo que el archivo funcione sin recursos externos

Para ejecutar y que se genere un archivo HTML en la carpeta raiz
```bash
python -m run_tests.py
```

## Logs de ejecucion

El logging nos permite registrar de forma cronológica todo lo que sucede durante la ejecución de nuestras pruebas

## Captura de pantalla 

Se realizan capturas de pantalla en cada test que haya registrado un fallo y se visualizan en la carpeta reports/screens

## Descripción de las pruebas 

- Test de Login
- Test de Navegación
- Test de Carga del Carrito
- Test de carga del carrito version con json
- Test de apis
