import undetected_chromedriver as uc 
import time
import json
import notify
from decouple import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)
from selenium.webdriver.support import expected_conditions as EC


def get_driver(headless):
    option = uc.ChromeOptions()
    chrome_prefs = {}
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
    chrome_prefs["credentials_enable_service"] = bool("")
    chrome_prefs["profile.password_manager_enabled"] = bool("")
    option.add_experimental_option('prefs', chrome_prefs)

    if headless:
        option.add_argument("--headless=True")
    #option.add_argument(r"--load-extension=C:\Users\BANARJI\Desktop\Upwork\In-Progress\Appen Scrape Bot\extension")
    
    option.add_argument("--log-level=0")
    driver = uc.Chrome(options=option) 
    return driver
def result_check(sem):
    sem = int(sem)+1
    driver.get("https://makaut1.ucanapply.com/smartexam/public/student/student-activity")
    wait.until(EC.presence_of_all_elements_located(("css selector","table#table>tbody>tr")))
    list = driver.find_elements("css selector","table#table>tbody>tr")
    if(len(list)==sem):
        return 1
    else:
        return 0

def makaut_login(rollno,password):
    driver.get("https://makaut1.ucanapply.com/smartexam/public/")
    print("Logging in")
    wait.until(EC.presence_of_element_located(('xpath','//span[contains(text(),"STUDENT")]'))).click()
    wait.until(EC.presence_of_element_located(('css selector','input#username'))).send_keys(rollno)
    wait.until(EC.presence_of_element_located(('css selector','input#password'))).send_keys(password)
    wait.until(EC.presence_of_element_located(('xpath','//*[contains(text(),"Submit")]'))).click()
    wait.until(EC.presence_of_all_elements_located(('css selector','ul.btn-circle')))
    print("Logged in")

driver = get_driver(False)
ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
wait = WebDriverWait(driver,timeout=60,poll_frequency=2,ignored_exceptions=ignore_list)
rollno=config("uniroll")
sem=config("sem")
password=config("pass")
makaut_login(rollno,password)
while True:
    res = result_check(sem)
    if res==1:
        notify.send()
        break
    else:
        print("Not published yet,refreshing")

