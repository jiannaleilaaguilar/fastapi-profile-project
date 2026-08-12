# FastAPI User Profile Management Feature

A full-stack user profile management system built with **FastAPI**, **SQLAlchemy**, **Pydantic**, and **SQLite**. Features secure password hashing, a responsive front-end UI, automated test suites (Unit, Integration, E2E with Playwright), and a **GitHub Actions CI/CD pipeline** for automated testing and Docker container deployment.

---

## 🚀 Repository Links
* **GitHub Repository:** [https://github.com/jiannaleilaaguilar/fastapi-profile-project](https://github.com/jiannaleilaaguilar/fastapi-profile-project)
* **Docker Hub Repository:** [https://hub.docker.com/r/jiannaleila/fastapi-profile-app](https://hub.docker.com/r/jiannaleila/fastapi-profile-app)

---

## ✨ Key Features
* **Profile Management:** View and update user profile information (Username, Email).
* **Secure Password Change:** Verify current password using Bcrypt before updating.
* **Data Validation:** Input validation using Pydantic v2 schemas.
* **Front-End UI:** Static HTML/JS interface with real-time alert notifications and async fetch API integrations.
* **Comprehensive Testing:** Automated Unit, Integration, and Playwright E2E testing suites.
* **CI/CD Automation:** Automated pytest execution and Docker Hub container deployment via GitHub Actions.

---

## 🛠️ Local Setup & Running

### 1. Prerequisites & Installation
```bash
# Clone the repository
git clone [https://github.com/jiannaleilaaguilar/fastapi-profile-project.git](https://github.com/jiannaleilaaguilar/fastapi-profile-project.git)
cd fastapi-profile-project

# Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate  # On Linux/Mac: source venv/bin/activate

# Install dependencies and Playwright browser binaries
pip install -r requirements.txt
python -m playwright install --with-deps chromium
