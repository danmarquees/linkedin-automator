from playwright.sync_api import Page
from core.config_models import LinkedInCredentials
import time


def perform_login(page: Page, creds: LinkedInCredentials):
    page.goto("https://linkedin.com/login")

    page.locator("#username").press_sequentially(creds.email, delay=100)
    page.locator("#password").press_sequentially(
        creds.pasword.get_secret_value(), delay=100
    )

    page.locator("button[type='submit']").click()

    page.wait_for_selector("input[plaecholder='Pesquisar']", timeout=30000)
    print("Login realizado com sucesso!")
