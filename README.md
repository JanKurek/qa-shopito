# 🧪 QA Shopito – Automated Testing Framework

## 📖 About the Project
**QA Shopito** is a complete test automation framework for both **API** and **UI** testing.  
It combines **Python (pytest + requests)** for backend validation and **Playwright (TypeScript)** for frontend automation.  
All tests are integrated into a **CI/CD pipeline** using **GitHub Actions**, running automatically on every push.

---

## ⚙️ Technologies
- 🐍 **Python 3.11**
- 🧪 **Pytest** – API testing
- 🌐 **Requests** – HTTP requests handling
- 🎭 **Playwright** – UI automation
- ⚙️ **GitHub Actions** – CI/CD pipeline
- 💡 **TypeScript** – for UI test configuration

---

## 🧩 Project Structure
```
qa-shopito/
├── conftest.py # Fixtures for API tests
├── test_users_api.py # API tests (dummyjson.com)
├── tests_ui/
│ ├── smoke.spec.ts # UI smoke test (Demoblaze)
│ └── playwright.config.ts # Playwright configuration
├── .github/workflows/ci.yml # CI/CD pipeline definition
├── requirements.txt # Python dependencies
├── package.json # Node dependencies
└── README.md # Project documentation 
```


### 🔹 API Tests
```bash
pytest -v
# or only API-marked tests:
pytest -m api -v
```

### 🔹 UI Tests
```bash
npx playwright install
npx playwright test
# or with a specific base URL:
$env:UI_BASE_URL="https://www.demoblaze.com/"; npx playwright test
```


🔄 CI/CD Workflow

Every push or pull request automatically triggers:

API tests using pytest

UI tests using Playwright

HTML report generation as GitHub artifact

📊 CI Status

📬 Author
Ján Kurek
📍 Slovakia
💼 LinkedIn Profile
🌐 [GitHub Profile](https://github.com/JanKurek)
