from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from config import GIFTS_UNDER_25_XPATH, ITEM_CONTAINER_XPATH, ELEMENT_WAIT_TIMEOUT, PAGE_LOAD_WAIT


@step('Navigate to the target website')
def navigate_to_target(context):
    context.driver.get(context.url)


@step('Click on gifts under 25')
def click_under_25(context):
    under_25 = context.driver.find_element(By.XPATH, GIFTS_UNDER_25_XPATH)
    under_25.click()
    WebDriverWait(context.driver, PAGE_LOAD_WAIT).until(
        EC.presence_of_all_elements_located((By.XPATH, ITEM_CONTAINER_XPATH))
    )


@step('Check if all gifts are under 25')
def verify_gifts_under_25(context):
    items = WebDriverWait(context.driver, ELEMENT_WAIT_TIMEOUT).until(
        EC.presence_of_all_elements_located((By.XPATH, ITEM_CONTAINER_XPATH))
    )
    issues = []
    for item in items:
        price_text = item.get_attribute("current-price")
        if price_text:
            try:
                price = float(price_text.replace("$", "").replace(",", ""))
                if price > 25.00:
                    issues.append(price)
            except ValueError:
                continue
    assert len(issues) == 0, f"Found {len(issues)} items over $25: {issues}"
