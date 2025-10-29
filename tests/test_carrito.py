from selenium.webdriver.common.by import By
from selenium import webdriver

def test_carrito(login_in_driver):
    try:
        driver = login_in_driver

        productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        # Añadir el primer producto al carrito
        productos[0].find_element(By.TAG_NAME, 'button').click()
        # Confirmar que el badge del carrito muestra 1
        badge = driver.find_element(By.CLASS_NAME,'shopping_cart_badge').text
        assert badge == '1'
        print('Carrito OK →', badge)
    except Exception as e:
        print(f"Error en test_navegacion: {e}")
        raise
    finally:
        driver.quit()




