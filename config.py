import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

# Target URLs
TARGET_URL = os.getenv("TARGET_URL", "https://www.target.com/c/gift-ideas-for-women/-/N-22vn7")

# Timeouts
ELEMENT_WAIT_TIMEOUT = int(os.getenv("ELEMENT_WAIT_TIMEOUT", "10"))
PAGE_LOAD_WAIT = int(os.getenv("PAGE_LOAD_WAIT", "5"))

# XPath selectors
GIFTS_UNDER_25_XPATH = "//div[@class='sc-710d0ece-2 ixDA-dd'][span[text() = 'Gifts under $25']]"
ITEM_CONTAINER_XPATH = "//div[@class='sc-f82024d1-0 rLjwS']"

# Screenshot directory
SCREENSHOT_DIR = BASE_DIR / "screenshots"
