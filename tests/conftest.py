import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_setup_options():
    """Configure Chrome options for pytest-dash"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options


@pytest.fixture(scope='session', autouse=True)
def configure_webdriver():
    """Install and configure ChromeDriver once per session"""
    import os
    driver_path = ChromeDriverManager().install()
    # Add driver directory to PATH so pytest-dash can find it
    driver_dir = str(Path(driver_path).parent)
    os.environ['PATH'] = driver_dir + os.pathsep + os.environ['PATH']
    yield