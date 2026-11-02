import pytest
from selenium import webdriver
from login_page import LoginPage

def test_login_fallido(controlador):
    """Prueba de usuario bloqueado (Con fallo intencional para verificar la captura)"""
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()
    
    # ❌ FALLO FORZADO: Texto incorrecto para obligar a que falle la prueba y tome la foto
    assert "Texto inventado que provocará un fallo" in login.obtener_error() 

def test_login_exitoso(controlador):
    """Prueba de login correcto"""
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()
    assert "inventory.html" in driver.current_url
