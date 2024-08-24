import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from logs.logging_config import logging

def setup_browser():
    try:
        # Set up the browser options
        options = Options()
        options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data")
        options.add_argument("--profile 3")
        options.add_argument("--disable-tflite-xnnpack")
        logging.info(f"Load User profile : C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\profile 3")
        # Set up the browser service
        service = Service(ChromeDriverManager().install())

        # Launch the browser
        driver = webdriver.Chrome(service=service, options=options)

        # Navigate to WhatsApp
        driver.get("https://web.whatsapp.com/")
        logging.info(f"Goto : https://web.whatsapp.com/")
        # Wait for WhatsApp Web to load completely
        return driver
    except Exception as e:
        logging.info(f"Error setting up browser: {e}")
        return None

def send_message(driver, phone_numbers, message):
    for phone_number in phone_numbers:
        logging.info(f"Sending message to {phone_number}: {message}")
        try:
            # Click on the new chat button
            new_chat_button = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@title='New chat']")))
            new_chat_button.click()
            logging.info(f"{phone_number}: new_chat_button.click()")
            # Enter the phone number
            phone_number_input = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Search name or number']")))
            phone_number_input.send_keys(phone_number)
            logging.info(f"{phone_number}: input phone_number")

            chats_xpath = "//div[contains(text(), 'Contacts on WhatsApp')]"
            chat_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, chats_xpath)))
            # Get search result
            logging.info(f"{phone_number}: find Contacts on WhatsApp")
            _element = chat_element.find_element(By.XPATH, "ancestor::*[2]")
            parent_element = _element.find_element(By.XPATH, "ancestor::*[1]")
            # Wait for the parent element to be visible
            WebDriverWait(driver, 30).until(EC.visibility_of(parent_element))
            time.sleep(5)  # wait for 1 second
            
            direct_child_divs = parent_element.find_elements(By.XPATH, "div")
            last_child_div = direct_child_divs[-1]
            
            time.sleep(5)
            last_child_div.click()
            logging.info(f"{phone_number}: contact.click()")
            time.sleep(5)
            type_a_message = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Type a message']"))
            )
            
            type_a_message.click()
            logging.info(f"{phone_number}: type_a_message.click()")
            actions = ActionChains(driver)
            actions.send_keys_to_element(type_a_message, message)
            logging.info(f"{phone_number}: type_a_message.send_keys_to_element()")
            actions.perform()
            time.sleep(5)
            send_button_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button [@aria-label='Send']"))
            )
            send_button_div.click()
            logging.info(f"{phone_number}: send_button_div.click()")
            time.sleep(5)

        except Exception as e:
            logging.info(f"Error sending message to {phone_number}: {e}")
