from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Whatsapp:
    def __init__(self) -> None:
        """The class helps you to send messages by using function findReciepient and sendto target"""
        option = Options()
        option.add_experimental_option("detach", True)
        option.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3641.0 Safari/537.36')
        option.add_argument("--user-data-dir=user-data")
        self.__driver = webdriver.Chrome(
            "drivers/chromedriver", options=option)
        self.__driver.get("https://web.whatsapp.com")
        self.__wait = WebDriverWait(self.__driver, 600)

    def findReciepient(self, target):
        """Enter in chat of the target"""
        x_arg = f'//span[@title= "{target}"]'
        cur = self.__wait.until(EC.element_to_be_clickable((By.XPATH, x_arg)))
        cur.click()

    def sendToTarget(self, message="Hi"):
        """send the message to the chat open"""
        inpBox = self.__driver.find_element_by_xpath("//div[@class= '_2A8P4']")
        inpBox.send_keys(message)
        time.sleep(0.5)
        inpBox.send_keys(Keys.RETURN)
        time.sleep(0.5)

    def quit(self):
        """Quits the automated session"""
        self.__driver.quit()
