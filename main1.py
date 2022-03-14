web_url ="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import  NoSuchElementException

chrome_driver_path ="C:/Users/hudayis/Documents/Development/chromedriver.exe"

ser = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get(web_url)

find_login = driver.find_element(By.XPATH,"/html/body/div[1]/header/nav/div/a[2]")
find_login.click()

find_username_area = driver.find_element(By.ID, "username")
find_username_area.send_keys("mmanusx@gmail.com")
find_password_area = driver.find_element(By.ID, "password")
find_password_area.send_keys("161816181618Mhs.")

find_login_button = driver.find_element(By.CLASS_NAME,"login__form_action_container")
find_login_button.click()

find_firs_job_in_list = driver.find_element(By.CSS_SELECTOR, ".job-card-list_entity-lockup .artdeco-entity-lockup")
find_firs_job_in_list.click()

#time.sleep(5)
apply_to_job = driver.find_element(By.CSS_SELECTOR, "div.jobs-apply-button--top-card button.jobs-apply-button")
apply_to_job.click()