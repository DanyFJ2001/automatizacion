from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://login.microsoftonline.com/0ed76805-9b6f-44ec-bcfe-98ad9efc9788/oauth2/v2.0/authorize?response_type=code&client_id=5c799b6d-03e6-4852-a15c-630e7442289b&redirect_uri=https://campusvirtual.itsqmet.edu.ec/campusV/authentication/login-callback&scope=https://graph.microsoft.com/User.Read&state=ThislsMyStateValue")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))

username_input = driver.find_element(By.XPATH, '//input[@type="email"]') 
username_input.send_keys("dfernandez@itsqmet.edu.ec")
boton_login = driver.find_element(By.XPATH, '//input[@type="submit"]')
boton_login.click()
time.sleep(5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))

password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
password_input.send_keys("Itsqmet1751058312")
time.sleep(5)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="submit"]')))
boton_login = driver.find_element(By.ID, "idSIButton9")
boton_login.click()
time.sleep(5)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="idBtn_Back"]')))
boton_mantener_sesion = driver.find_element(By.XPATH, '//input[@id="idBtn_Back"]')
boton_mantener_sesion.click()

time.sleep(10)

driver.get("https://virtual3.itsqmet.edu.ec:84/")
time.sleep(15)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-course-id="7126"]//button[contains(@class, "rui-course-card-link")]')))

boton_ingresar = driver.find_element(By.XPATH, '//div[@data-course-id="7126"]//button[contains(@class, "rui-course-card-link")]')
driver.execute_script("arguments[0].scrollIntoView(true);", boton_ingresar)
time.sleep(2)
boton_ingresar.click()

time.sleep(10)

WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-key="grades"]//a[contains(text(), "Calificaciones")]')))
calificaciones_link = driver.find_element(By.XPATH, '//li[@data-key="grades"]//a[contains(text(), "Calificaciones")]')
driver.execute_script("arguments[0].click();", calificaciones_link)

time.sleep(30)