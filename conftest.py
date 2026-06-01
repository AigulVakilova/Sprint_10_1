import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_taxi_page import OrderTaxiPage
from pages.search_page import SearchPage
import data
import urls

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open(urls.BASE_URL)
    return page

@pytest.fixture
def route_page(driver):
    return RoutePage(driver)

@pytest.fixture
def order_taxi_page(driver):
    return OrderTaxiPage(driver)

@pytest.fixture
def search_page(driver):
    return SearchPage(driver)

@pytest.fixture
def pages_with_two_addresses(main_page, route_page):
    main_page.set_address_from(data.ADDRESS_FROM)
    main_page.set_address_to(data.ADDRESS_TO)
    return main_page, route_page

@pytest.fixture
def pages_with_same_address(main_page, route_page):
    main_page.set_address_from(data.ADDRESS_FROM)
    main_page.set_address_to(data.ADDRESS_SAME)
    return main_page, route_page

@pytest.fixture
def pages_ready_for_taxi_order(main_page, route_page, order_taxi_page):
    main_page.set_address_from(data.ADDRESS_FROM)
    main_page.set_address_to(data.ADDRESS_TO)
    route_page.click_route_fast()
    route_page.click_call_taxi()
    order_taxi_page.wait_for_order_form()
    return main_page, route_page, order_taxi_page
