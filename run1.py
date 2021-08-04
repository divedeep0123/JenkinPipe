from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome('C:\\Users\\hrdeepak\\PycharmProjects\\chromedriver.exe')
driver.get("http://localhost/webapp/eSignageS/login/tenant.ejs")
driver.maximize_window()
driver.find_element_by_id("auth_login_id").send_keys("admin")
driver.find_element_by_id("auth_password").send_keys("admin")
driver.find_element_by_name("auth_login").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div/div[2]/img").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div[8]/a").click()
time.sleep(2)
driver.find_element_by_id("createFolderBtn").click()
time.sleep(2)
driver.switch_to.frame(driver.find_element_by_id("btn_SelectedPlayerNormal").click())
element=driver.find_element_by_id("dd_folderType")
drp=Select(element)
driver.close()