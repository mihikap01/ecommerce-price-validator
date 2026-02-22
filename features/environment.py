import os
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config


def before_feature(context, feature):
    context.url = config.TARGET_URL


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def after_step(context, step):
    if step.status == 'failed':
        screenshot_dir = str(config.SCREENSHOT_DIR)
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f'{step.name}.png')
        print(screenshot_path)
        context.driver.save_screenshot(screenshot_path)


def after_scenario(context, scenario):
    try:
        context.driver.close()
    except Exception:
        pass
    try:
        context.driver.quit()
    except Exception:
        pass
