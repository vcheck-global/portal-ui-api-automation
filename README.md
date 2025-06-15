# portal-ui-api-automation

# Hybrid UI + API Automation Framework

This project is designed to test both **UI and API** functionalities of the `revamp-qa-admin-api.vcheckglobal.net` and `revamp-qa.vcheckglobal.net` platforms using Playwright (for UI) and `requests`/custom libraries (for API). It integrates Salesforce (SF) test data and utility methods via a reusable library.

---

## 🔧 Features

- ✅ Hybrid UI and API test coverage
- ✅ Playwright-based UI automation with Page Object Model (POM)
- ✅ API test integration with reusable AuthHandler and SF libraries
- ✅ Token-based authentication (multi-step)
- ✅ Environment and credential management via `.env`
- ✅ HTML reporting support
- ✅ Clean structure ready for CI/CD

---

## 📁 SF Libraries Dependency

This project reuses shared libraries for Salesforce interaction from the [sf-api-automation](https://github.com/vcheck-global/sf-api-automation) repository.

---

## 🚀 Installation

### 1. Clone this repository:

```bash
git clone https://github.com/vcheck-global/portal-ui-api-automation.git
cd portal-ui-api-automation


### 2. Create a virtual environment (recommended):
python -m venv venv

### 3. Activate the virtual environment:
* Windows
venv\Scripts\activate
*macOS/Linux:
source venv/bin/activate

### 4. Install project dependencies:
pip install -r requirements.txt

Reuse SF API Automation as a Python Library:

To install the Salesforce test data/util libraries from the sibling repo:

pip install -e ../sf-api-automation
Make sure the relative path is correct based on your project structure.

Running the Tests
Run a specific test file like this:
pytest tests/test_login_flow_api.py
You can generate reports using pytest-html if configured.

### Environment Variables
Configure sensitive data and URLs in a .env file:
EMAIL=your_email@example.com
PASSWORD=your_password
LOGIN_URL=https://revamp-qa.vcheckglobal.net/login
