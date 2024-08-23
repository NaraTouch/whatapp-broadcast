import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def setup_browser():
    try:
        # Set up the browser options
        options = Options()
        options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument("--profile 3")
        options.add_argument("--disable-tflite-xnnpack")

        # Set up the browser service
        service = Service(ChromeDriverManager().install())

        # Launch the browser
        driver = webdriver.Chrome(service=service, options=options)

        # Navigate to WhatsApp
        driver.get("https://web.whatsapp.com/")

        # Wait for WhatsApp Web to load completely
        New_chat = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@title='New chat']")))
        return driver
    except Exception as e:
        print(f"Error setting up browser: {e}")
        return None

def send_message(driver, phone_number, message):
    try:
        # Click on the new chat button
        new_chat_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@title='New chat']")))
        new_chat_button.click()

        # Enter the phone number
        phone_number_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Search name or number']")))
        phone_number_input.send_keys(phone_number)

        chats_xpath = "//div[contains(text(), 'Contacts on WhatsApp')]"
        chat_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, chats_xpath)))
        # Get search result
        _element = chat_element.find_element(By.XPATH, "ancestor::*[2]")
        parent_element = _element.find_element(By.XPATH, "ancestor::*[1]")
        # Wait for the parent element to be visible
        WebDriverWait(driver, 30).until(EC.visibility_of(parent_element))
        time.sleep(10)  # wait for 1 second
            
        direct_child_divs = parent_element.find_elements(By.XPATH, "div")
        last_child_div = direct_child_divs[-1]
        print(last_child_div.get_attribute("outerHTML"))
        time.sleep(10)
        last_child_div.click()
        time.sleep(10)
        # type_a_message_xpath = "//div[@aria-label='Type a message' and @visibility='visible']"
        # type_a_message = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, type_a_message_xpath)))
        # print(type_a_message.get_attribute("outerHTML"))

        # type_a_message.send_keys(message)
        # print(last_child_div.get_attribute("outerHTML"))
         # prints the number of child div elemen

    except Exception as e:
        print(f"Error sending message: {e}")
