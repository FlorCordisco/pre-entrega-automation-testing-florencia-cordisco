# pre-entrega-automation-testing-florencia-cordisco
Repositorio creado para realizar una pre-entrega para el curso Automation Testing dictado por Agencia de Habilidades para el Futuro de Buenos Aires Aprende

El propósito del proyecto es dar a conocer lo aprendido hasta el momento (clase 8),
donde se desarrollan test de el login y la navegación básica de la web:

             saucedemo.com
Datos: usuario: "standard_user", contraseña: "secret_sauce"            

## Tecnologías Requeridas:

-Python como lenguaje principal

-Pytest para estructura de testing: instalar desde la terminal con el comando 
pip install pytest-html

-Selenium WebDriver para automatización: desde la terminal instalar 
pip install selenium
pip install webdriver-manager

-Git y GitHub para control de versiones

## Reporte en HTML
Instalar: pip install pytest-html
Ejecutar: pytest --html=report.html --self-contained-html

--html=report.html establece el nombre del archivo
--self-contained-html incrusta CSS y JS, de modo que el archivo funcione sin recursos externos

## Descripción de las pruebas 

- Test de Login
- Test de Navegación
- Test de Carga del Carrito
