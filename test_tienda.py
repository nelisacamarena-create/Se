from login_page import LoginPage

def test_login_fallido(controlador):
    """Prueba de login fallido con aserción intencional para generar captura"""
    driver = controlador
    driver.get("https://www.saucedemo.com/")
    
    login = LoginPage(driver)
    login.iniciar_sesion("locked_out_user", "secret_sauce")
    
    # Mensaje de fallo intencional para verificar la captura en el reporte HTML
    assert "Texto inventado que provocará un fallo" in login.obtener_error()

def test_login_exitoso(controlador):
    """Prueba de login correcto"""
    driver = controlador
    driver.get("https://www.saucedemo.com/")
    
    login = LoginPage(driver)
    login.iniciar_sesion("standard_user", "secret_sauce")
    
    # Validación de éxito
    assert "inventory.html" in driver.current_url
