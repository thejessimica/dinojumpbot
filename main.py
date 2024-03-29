from PIL import Image
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
url = "https://elgoog.im/dinosaur-game/"
driver.get(url)
driver.maximize_window()

time.sleep(3)

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.SPACE)

game_on = True


def check_obstacle(image_paths, region, confidence):
    for image_path in image_paths:
        try:
            obstacle_location = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=confidence, region=region)
            print(obstacle_location.left)
            if obstacle_location.left <= 280:
                body.send_keys(Keys.SPACE)
                print(f"Attempted jump. Obstacle location: {obstacle_location.left}")
                return True
        except pyautogui.ImageNotFoundException:
            pass
    return False


while game_on:
    # Daytime cacti
    day_cactus_images = ['images/cactus_day.png', 'images/cactus_day_left_up.png', 'images/cactus_day_right_up.png']
    day_cactus_region = (200, 620, 200, 150)
    day_cactus_confidence = 0.2
    if check_obstacle(day_cactus_images, day_cactus_region, day_cactus_confidence):
        continue
