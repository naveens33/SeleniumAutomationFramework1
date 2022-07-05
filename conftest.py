import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=True)
def driver(request, get_caps):
    driver_ = None
    if get_caps["browser"] == "chrome":
        driver_ = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),desired_capabilities=get_caps["caps"])
        driver_.maximize_window()
        driver_.get('http://zero.webappsecurity.com/')
        sign_in_button = driver_.find_element(By.ID, 'signin_button')
        sign_in_button.click()
        driver_.find_element(By.ID, 'user_login').send_keys('username')
        driver_.find_element(By.ID, 'user_password').send_keys('password')
        driver_.find_element(By.NAME, 'submit').click()
    else:
        raise
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com/")

    def cleanup():
        driver_.quit()
        pass

    request.addfinalizer(cleanup)

    return driver_


@pytest.fixture(scope="class")
def search_page_fixture(request, driver):
    request.cls.driver = driver
    # request.cls.navbar.navigate_to_search_page()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="option: chrome or firefox", choices=("chrome", "firefox")
    )


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def get_caps(request, browser):
    import json
    f = open(r'C:\Users\Naveen S\PycharmProjects\automationframework1\capabilities\caps.json')
    data = json.load(f)
    options = None
    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.page_load_strategy = data['page_load_strategy']
    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options
        options = Options()
    else:
        pass
    caps = options.to_capabilities()
    return {"browser": browser, "caps": caps}
