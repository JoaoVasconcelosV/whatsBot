from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contacts = ['João', 'Amor❤️']
message = 'Testando o bot! My love'

def seek_contact(contact):
    research_field = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')    
    research_field.click()
    time.sleep(3)
    research_field.send_keys(contact)
    research_field.send_keys(Keys.ENTER)

def send_message(message):
    research_field = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    research_field[1].click()
    time.sleep(3)
    research_field[1].send_keys(message)
    research_field[1].send_keys(Keys.ENTER)


for contact in contacts:
    seek_contact(contact)
    send_message(message)