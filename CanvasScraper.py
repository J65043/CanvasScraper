import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions

# Replace with your Canvas login credentials
CANVAS_USERNAME = ""
CANVAS_PASSWORD = ""

# Replace with your course code and Canvas URL
COURSE_CODE = ""
CANVAS_URL = ""

def attachment_handling(driver):
    attachments = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "attachment"))
    )

    for attachment in attachments:
        item_button = attachment.find_element(By.CLASS_NAME, "ig-title")
        print(item_button.text)
        link = item_button.get_attribute("href")
        driver.get(link)

        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@download='true']"))
        )
        downloads = driver.find_elements(By.XPATH, "//a[@download='true']")
        for download in downloads:
            download.click()

        driver.back()

def process_assignments(driver):
    assignments = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "ig-row"))
    )

    for assignment in assignments:
        icon = assignment.find_element(By.CLASS_NAME, "type_icon")
        if icon.get_attribute("title") in ["Attachment", "Page"]:
            link = assignment.find_element(By.CLASS_NAME, "ig-title")
            link.click()

            if icon.get_attribute("title") == "Attachment":
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@download='true']"))
                )
                download_link = driver.find_element(By.XPATH, "//a[@download='true']")
                download_link.click()
            elif icon.get_attribute("title") == "Page":
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "file_download_btn"))
                    )
                    downloads = driver.find_elements(By.CLASS_NAME, "file_download_btn")
                    for download in downloads:
                        download.click()
                except exceptions.TimeoutException:
                    print("No downloadable content on page.")

            driver.back()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get(f"{CANVAS_URL}")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(CANVAS_USERNAME)
    driver.find_element(By.ID, "password").send_keys(CANVAS_PASSWORD, Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "duo_iframe")))
    driver.switch_to.frame(driver.find_element(By.ID, "duo_iframe"))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send Me a Push']"))).click()
    driver.switch_to.default_content()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ic-DashboardCard__header")))
    driver.get(f"{CANVAS_URL}/courses/{COURSE_CODE}/modules")

    process_assignments(driver)

    print("quitting browser")
    driver.quit()

if __name__ == "__main__":
    main()
