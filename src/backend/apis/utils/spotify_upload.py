import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.backend.core.config import settings
from src.backend.apis.utils.web import start_web


def start_uploading(path, descriptions):
    try:
        driver = start_web()
        wait = WebDriverWait(driver, 100)
        login(driver, wait)
        for file_name in os.listdir(path):
            upload_files(driver, wait, path, file_name)
            input_details(driver, descriptions, file_name)

        return True
    except:
        return False


def login(driver, wait):
    driver.get("https://podcasters.spotify.com/pod/dashboard/episode/wizard")

    driver.find_element(
        By.XPATH, '//*[@id="app-content"]/div/div[3]/div/button[1]'
    ).click()

    username = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    password = driver.find_element(By.NAME, "password")

    username.send_keys(settings.USER)
    password.send_keys(settings.PWD)
    username.submit()  # Submit Login


def upload_files(driver, wait, path, file_name, refresh=True):
    try:
        uploadepisode = wait.until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
        )
        uploadepisode.send_keys(os.path.join(path, file_name))
    except:
        if refresh:
            print("Refreshed Browser")
            driver.refresh()
            upload_files(driver, wait, path, file_name, False)
        else:
            # driver.save_screenshot("image.png")
            raise TimeoutError("Browser not responsive.")

    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//*[@id="app-content"]/div/div/footer/div/div[3]/div/span'),
            "Preview ready!",
        )
    )


def input_details(driver, descriptions, file_name):
    title = driver.find_element(By.NAME, "title")
    title.send_keys(file_name[:-4])

    textbox = driver.find_element(By.NAME, "description")
    textbox.send_keys(descriptions[file_name[:-4]])

    publishRadio = driver.find_element(By.ID, "publish-date-now")
    driver.execute_script("arguments[0].checked = true;", publishRadio)

    explicitRadio = driver.find_element(By.ID, "no-explicit-content")
    driver.execute_script("arguments[0].checked = true;", explicitRadio)

    nextButton1 = driver.find_element(
        By.XPATH, '//*[@id="app-content"]/div/div/footer/div/div[4]/button'
    )
    driver.execute_script("arguments[0].click();", nextButton1)
    time.sleep(3)
    nextButton2 = driver.find_element(
        By.XPATH, '//*[@id="app-content"]/div/div/footer/div/div[4]/button'
    )
    driver.execute_script("arguments[0].click();", nextButton2)
    time.sleep(3)
    publishBut = driver.find_element(
        By.XPATH, '//*[@id="app-content"]/div/div/footer/div/div[4]/button'
    )
    driver.execute_script("arguments[0].click();", publishBut)

    driver.get("https://podcasters.spotify.com/pod/dashboard/episode/wizard")
