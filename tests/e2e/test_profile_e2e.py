import pytest
import uvicorn
import threading
import time
from playwright.sync_api import Page, expect
from app.main import app

@pytest.fixture(scope="module", autouse=True)
def run_server():
    # Start background server for E2E testing
    config = uvicorn.Config(app, host="127.0.0.1", port=8001, log_level="error")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run)
    thread.daemon = True
    thread.start()
    time.sleep(1)  # Allow server to start
    yield
    server.should_exit = True

def test_profile_page_renders_correctly(page: Page):
    # Navigate to the local static page
    page.goto("http://127.0.0.1:8001/static/profile.html")
    
    # Assert main headers and input fields are visible
    expect(page.locator("h2").first).to_contain_text("User Profile")
    expect(page.locator("#username")).to_be_visible()
    expect(page.locator("#email")).to_be_visible()
    expect(page.locator("#currentPassword")).to_be_visible()
    expect(page.locator("#newPassword")).to_be_visible()
