from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)



# Open a web page
s="getting"
URL = "https://cfi.iitm.ac.in/blog?search="+s

driver.get(URL)
time.sleep(2)
elem=driver.find_elements(By.TAG_NAME,'a')[2]
print(elem)
elem.click()
time.sleep(3)
#driver.quit()
