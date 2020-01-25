import pytest
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver_ = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver")
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com/")

    return driver_
