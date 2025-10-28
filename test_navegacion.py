from selenium.webdriver.common.by import By
from selenium import webdriver

def test_navegacion(login_in_driver):
    try:
        driver = login_in_driver

        assert driver.title == "Swag Labs"
        # contar productos visibles
        productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        assert len(productos) > 0, "No hay productos visibles en la pagina"
    except Exception as e:
        print(f"Error en test_navegacion: {e}")
        raise
    finally:
        driver.quit()