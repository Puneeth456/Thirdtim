# from selenium import webdriver
#
# driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
# driver.get("https://marvin.treebo.com/")
# driver.find_element_by_name("username").send_keys("Cluster_view")
# driver.find_element_by_name("password").send_keys("core13578!")
# driver.find_element_by_xpath("//button[contains(text(),'LOGIN')]").click()
# driver.find_element_by_xpath("//button[@type='button']").click()
# # driver.find_element_by_xpath("//a[@class='logout-link']").click()
# driver.find_element_by_xpath("//a[@href='/logout']").click()


from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/chromedriver.exe")
driver.get("https://jqueryui.com/")
driver.find_element_by_xpath("//a[text()='Datepicker']").click()
framewar=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to_frame(framewar)
driver.find_element_by_id("datepicker").click()
driver.find_element_by_xpath("//a[text()='14']")


