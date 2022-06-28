import pytest
from selenium import webdriver

from pom.homepage import HomePage


@pytest.fixture(scope="session", autouse=True)
def driver(request,browser):
    driver_ = None
    if browser == "chrome":
        driver_ = webdriver.Chrome(r'C:\Users\Naveen S\Downloads\chromedriver_win32 (1)\chromedriver.exe')
    else:
        raise
    driver_.maximize_window()
    driver_.get("http://zero.webappsecurity.com/")

    def cleanup():
        driver_.quit()
        pass

    request.addfinalizer(cleanup)

    return driver_


@pytest.fixture(scope="module", params=[("username", "password")])
def login(request, driver):
    home = HomePage(driver)
    home.click_sign_in_button()
    #home.click_sign_in_button()
    #login = LoginPage(driver)
    #login.do_login(request.param[0],request.param[1])
    pass


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="option: chrome or firefox", choices=("chrome", "firefox")
    )

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
