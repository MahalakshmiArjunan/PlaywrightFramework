# Playwright Automation Framework

A practical end-to-end test automation framework built with Python and Playwright, covering UI automation, REST API testing, and integrated reporting. Built against real-world applications — SauceDemo for UI flows and the Restful Booker API for backend contract testing.

---

## What's inside

The framework is split into two testing layers that can be run independently or together:

**UI Testing** — automates the full purchase journey on SauceDemo (login → add to cart → checkout → order confirmation) using the Page Object Model pattern. Test data is read from Excel, configuration from an ini file, keeping tests completely data-driven.

**API Testing** — covers the complete lifecycle of a hotel booking on the Restful Booker API: create a booking, retrieve by ID, search by name, authenticate, and perform an update. Each operation is a separate test with assertion on the response body fields.

---

## Project layout

```
PlaywrightFramework/
├── API/
│   ├── E2EHerokuAPITests.py       # Full booking lifecycle test suite
│   ├── E2EHerokuRequests.py
│   ├── postData.json              # Create booking payload
│   ├── updatePostData.json        # Update booking payload
│   └── auth.json                  # Auth credentials
├── pages/
│   ├── loginPage.py               # SauceDemo login interactions
│   ├── homePage.py                # Product listing and cart actions
│   ├── cartPage.py                # Cart review and checkout trigger
│   ├── infoPage.py                # Shipping info form
│   └── overviewPage.py            # Order summary and placement
├── tests/
│   └── test_E2EScenario1.py       # End-to-end purchase flow test
├── testData/
│   └── userInfo.xlsx              # Test credentials via Excel
├── utilities/
│   ├── ConfigReader.py            # Reads config.ini values
│   └── ExcelData.py               # Reads cell data from Excel
├── reports/
│   ├── report.html                # HTML test report
│   └── allure-results/            # Allure report raw data
├── conftest.py                    # Browser setup and page fixtures
├── pytest.ini                     # Global test configuration
└── main.py
```

---

## Tech stack

| Tool | Purpose |
|---|---|
| Python 3.13 | Core language |
| Playwright (sync API) | Browser automation and API request handling |
| Pytest | Test runner with fixtures and markers |
| Pytest-HTML | HTML test reports |
| Allure | Rich test reporting with traces and screenshots |
| OpenPyXL | Excel-based test data reading |
| ConfigParser | External configuration management |

---

## Getting started

**Prerequisites:** Python 3.10+, pip

```bash
# 1. Clone the repository
git clone https://github.com/MahalakshmiArjunan/PlaywrightFramework.git
cd PlaywrightFramework

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install playwright pytest pytest-playwright pytest-html allure-pytest openpyxl

# 4. Install browser binaries
playwright install chromium

# 5. Run UI tests
pytest tests/

# 6. Run API tests
pytest API/

# 7. Generate Allure report
allure serve reports/allure-results
```

---

## Configuration

The `pytest.ini` file controls run behaviour globally. Key settings:

```ini
--base-url=https://www.saucedemo.com     # Target app URL
--tracing=retain-on-failure              # Captures trace on failure
--video=retain-on-failure                # Records video on failure
--screenshot=only-on-failure             # Screenshot on failure
--alluredir=reports/allure-results       # Allure output path
```

To run in headless mode, remove `--headed` from `addopts`.

To run tests in parallel, uncomment `--numprocesses=2`.

---

## Test data

UI credentials are read from `testData/userInfo.xlsx`. The test picks username and password from row 2, columns 1 and 2 of Sheet1.

API payloads are stored as JSON files under `API/` — edit `postData.json` to change the booking details used across create and verify tests.

---

## Reports

After a test run, two report types are available:

- `reports/report.html` — open directly in a browser for a quick pass/fail summary with embedded screenshots
- `reports/allure-results/` — run `allure serve reports/allure-results` for the full interactive report with step-level traces, video, and timeline view

---

## Application under test

- **UI:** [SauceDemo](https://www.saucedemo.com) — a purpose-built demo e-commerce app
- **API:** [Restful Booker](https://restful-booker.herokuapp.com) — a public REST API for hotel booking management

---

## Author

**Mahalakshmi Arjunan**
QA Automation Engineer | Playwright · Python · API Testing · Allure
