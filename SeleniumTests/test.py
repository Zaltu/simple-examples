import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

profile_headless = Options()
profile_headless.add_argument("--headless")

driver = webdriver.Chrome(options=profile_headless)
print("Webdriver created...")
driver.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=fr&text=hello")
elem = driver.find_element_by_class_name("translation")
print(elem.text)
driver.close()
