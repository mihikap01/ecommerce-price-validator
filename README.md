# E-Commerce Price Validator

## What This Does

A BDD (Behavior-Driven Development) test suite that uses Selenium WebDriver to validate gift pricing on an e-commerce website. The suite navigates to a product category page, extracts all displayed prices, and asserts that every item in the "gifts under $25" section is actually priced at or below $25.00. Test scenarios are written in Gherkin syntax for readability, and screenshots are automatically captured on failure for debugging.

## How It Works

The test architecture has three layers:

1. **Feature Specification** (`gift_pricing.feature`): Gherkin-syntax `.feature` files define the test scenarios in plain English. Each scenario describes a user journey: navigate to the site, select a price-filtered category, and verify that all listed prices satisfy the constraint.

2. **Step Definitions** (`pricing_steps.py`): Python functions decorated with Behave's `@given`, `@when`, and `@then` map each Gherkin step to Selenium WebDriver actions. The driver navigates to `TARGET_URL`, clicks the category link via its XPath selector, extracts all price elements using a configured XPath expression, parses each price string into a float, and asserts that every value is less than or equal to 25.00. `WebDriverWait` with explicit conditions replaces hardcoded `sleep()` calls, ensuring the suite waits only as long as necessary for elements to load.

3. **Environment Hooks** (`environment.py`): Behave lifecycle hooks handle browser setup (launching a Chrome instance via `webdriver-manager`, which auto-downloads the correct ChromeDriver binary) and teardown (closing the browser after the suite completes). On any step failure, a timestamped screenshot is saved to the `screenshots/` directory.

All URLs, XPath selectors, and timeout values are defined in `config.py`, keeping step definitions free of hardcoded locators.

## Sample Output

Passing run:

```
$ behave features/
Feature: Gift Pricing Validation

  Scenario: Verify gifts under $25
    Given Navigate to the target website          # passed
    Then Click on gifts under 25                  # passed
    Then Check if all gifts are under 25          # passed

1 feature passed, 0 failed
1 scenario passed, 0 failed
3 steps passed, 0 failed
```

Failing run (price violation detected):

```
  Scenario: Verify gifts under $25
    Given Navigate to the target website          # passed
    Then Click on gifts under 25                  # passed
    Then Check if all gifts are under 25          # failed
    Assertion Failed: Found 3 items over $25: [29.99, 34.50, 27.99]
    Screenshot saved: screenshots/failed_step_2024-01-15_143022.png
```

## Quick Start

```bash
# Install dependencies and set up the environment
./setup.sh

# Run the full BDD test suite
behave features/
```

Google Chrome must be installed on the system. ChromeDriver is downloaded and managed automatically by `webdriver-manager` at runtime.

## Configuration

Edit `config.py` to adjust test parameters:

| Setting                | Description                                         |
|------------------------|-----------------------------------------------------|
| `TARGET_URL`           | Base URL of the e-commerce site under test          |
| `GIFTS_LINK_XPATH`     | XPath selector for the "gifts under $25" link       |
| `PRICE_ELEMENT_XPATH`  | XPath selector for individual product price elements|
| `ELEMENT_WAIT_TIMEOUT` | Maximum seconds to wait for page elements to load   |

## Project Structure

```
ecommerce-price-validator/
├── config.py                        # TARGET_URL, XPath selectors, timeouts
├── features/
│   ├── gift_pricing.feature         # BDD test scenarios (Gherkin syntax)
│   ├── environment.py               # Behave hooks (browser setup/teardown, screenshots)
│   └── steps/
│       └── pricing_steps.py         # Step definitions (navigate, click, validate prices)
├── screenshots/                     # Auto-captured on test failure
├── requirements.txt                 # Python dependencies
└── setup.sh                         # Environment setup script
```

## Dependencies

- behave
- selenium
- webdriver-manager
- python-dotenv
