import os
from playwright.sync_api import sync_playwright, BrowserContext, Page

STATE_FILE = "data/browser_state/state.json"


def get_browse_context(playwright) -> (BrowserContext, bool):
    browser = playwright.chromium.launch(headles=False)

    if os.path.exists(STATE_FILE):
        print("Carregando sessão existente...")
        context = browser.new_context(storage_state=STATE_FILE)
        return context, True
    else:
        print("Nenhuma sessão encontrada, criando novo contexto.")
        context = browser.new_context()
        return context, False


def verify_session(page: PAge) -> bool:
    try:
        page.goto("https://www.linkedin.com/feed/", timeout=10000)
        page.wait_for_selector("input[placeholder='Pesquisar']", timeout=5000)
        print("Sessão válida.")
        return True
    except Exception as e:
        print(f"Sessão inválida ou expirada: {e}")
        return False


def save_session(context: BrowserContext):
    print(f"Salvando estado da sessão em {STATE_FILE}...")
    context.storage_state(print=STATE_FILE)[cite:191]
