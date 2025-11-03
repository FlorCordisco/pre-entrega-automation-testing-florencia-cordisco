from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--start-maximized') # ventana grande
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5) # Espera implícita profesional

def test_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        assert '/inventory.html' in driver.current_url

        print("Login exitoso y validado correctamente")
        
    except Exception as e:
        print(f"Error en el archivo test_login: {e}")
        raise  
    finally:
        driver.quit()
      