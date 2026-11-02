import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def controlador():
    """Fixture del navegador configurada para entorno local y CI/CD (GitHub Actions)"""
    opciones = Options()
    
    # Opciones indispensables para que corra en el servidor Linux de GitHub Actions
    opciones.add_argument('--headless=new')
    opciones.add_argument('--no-sandbox')
    opciones.add_argument('--disable-dev-shm-usage')
    opciones.add_argument('--window-size=1920,1080')
    
    driver = webdriver.Chrome(options=opciones)
    yield driver
    driver.quit()
